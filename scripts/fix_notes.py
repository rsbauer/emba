import os
import re
import unicodedata

NOTES_DIR = "010 Notes"  # Update this if your notes folder has a different path

def sanitize_front_matter(content):
    """Fixes common YAML front matter issues like unquoted titles with colons."""
    if not content.startswith("---"):
        return content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return content

    fm_original = parts[1]
    body = parts[2]
    
    lines = fm_original.splitlines()
    fixed_lines = []
    for line in lines:
        if line.startswith("title:") and ":" in line[6:]:
            key, val = line.split(":", 1)
            val = val.strip()
            if not (val.startswith('"') and val.endswith('"')) and not (val.startswith("'") and val.endswith("'")):
                val_escaped = val.replace('"', '\\"')
                line = f'title: "{val_escaped}"'
        fixed_lines.append(line)

    fixed_fm = "\n".join(fixed_lines)
    return f"---{fixed_fm}---{body}"

def slugify(value):
    """Converts a string or path segment into a lowercase, URL-friendly slug."""
    value = str(value)
    # Normalize unicode characters
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    # Replace ampersands with 'and' for cleaner filenames
    value = value.replace('&', 'and')
    # Remove characters that aren't alphanumeric, spaces, hyphens, or slashes
    value = re.sub(r'[^\w\s\-/]', '', value)
    # Replace whitespace and multiple hyphens with a single hyphen
    value = re.sub(r'[-\s]+', '-', value).strip('-')
    return value.lower()

def slugify_target(target):
    """Handles wiki-link targets that may include subfolders (e.g., Folder/Note Name)."""
    parts = target.split('/')
    slugged_parts = [slugify(p) for p in parts]
    return '/'.join(slugged_parts)

def convert_wikilinks(body):
    """Converts Obsidian wiki-links to standard markdown links with slugified targets."""
    
    def replace_pipe(match):
        target = match.group(1).strip()
        label = match.group(2).strip()
        slug = slugify_target(target)
        return f'[{label}]({slug}.md)'

    def replace_simple(match):
        target = match.group(1).strip()
        slug = slugify_target(target)
        return f'[{target}]({slug}.md)'

    # Pattern for [[Target|Display Text]]
    pipe_pattern = re.compile(r'\[\[([^|\]]+)\|([^\]]+)\]\]')
    body = pipe_pattern.sub(replace_pipe, body)

    # Pattern for [[Target]]
    simple_pattern = re.compile(r'\[\[([^\]]+)\]\]')
    body = simple_pattern.sub(replace_simple, body)
    
    return body

def convert_callouts(body):
    """Converts Obsidian callouts (> [!NOTE]) into styled blockquotes."""
    callout_pattern = re.compile(r'>\s*\[!(\w+)\](?:\s+(.*))?')
    
    lines = body.splitlines()
    new_lines = []
    
    for line in lines:
        match = callout_pattern.match(line)
        if match:
            c_type = match.group(1).upper()
            c_title = match.group(2) or c_type
            new_lines.append(f"> **{c_title}**")
        else:
            new_lines.append(line)
            
    return "\n".join(new_lines)

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        original_content = f.read()

    content = sanitize_front_matter(original_content)
    
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            front_matter = f"---{parts[1]}---"
            body = parts[2]
            body = convert_wikilinks(body)
            body = convert_callouts(body)
            content = front_matter + body
    else:
        content = convert_wikilinks(content)
        content = convert_callouts(content)

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Sanitized: {file_path}")

def main():
    if not os.path.exists(NOTES_DIR):
        print(f"Directory {NOTES_DIR} not found. Skipping note sanitization.")
        return

    for root, _, files in os.walk(NOTES_DIR):
        for file in files:
            if file.endswith(".md"):
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
