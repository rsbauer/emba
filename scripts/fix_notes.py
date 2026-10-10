import os
import re

NOTES_DIR = "010 Notes"
note_map = {}

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

def build_note_map():
    """Scans notes and maps filenames to real relative paths."""
    if not os.path.exists(NOTES_DIR):
        return
    
    for root, _, files in os.walk(NOTES_DIR):
        for file in files:
            if file.endswith(".md"):
                rel_path = os.path.relpath(os.path.join(root, file), start=".")
                base_name = os.path.splitext(file)[0].lower()
                note_map[base_name] = rel_path
                note_map[file.lower()] = rel_path

def convert_wikilinks(body, current_file_path):
    """Converts Obsidian wiki-links to point to real file paths."""
    def replace_link(match):
        target = match.group(1).strip()
        label = match.group(2).strip() if match.lastindex >= 2 and match.group(2) else target
        
        lookup_key = os.path.basename(target).lower()
        if not lookup_key.endswith(".md"):
            lookup_key += ".md"
            
        if lookup_key in note_map:
            target_path = note_map[lookup_key]
            current_dir = os.path.dirname(current_file_path)
            rel_to_target = os.path.relpath(target_path, start=current_dir)
            rel_to_target = rel_to_target.replace("\\", "/")
            return f'[{label}]({rel_to_target})'
        else:
            return f'[{label}]({target}.md)'

    pattern = re.compile(r'\[\[([^|\]]+)(?:\|([^\]]+))?\]\]')
    return pattern.sub(replace_link, body)

def convert_callouts(body):
    """Converts Obsidian callouts into styled blockquotes."""
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

def wrap_in_raw(content):
    """Wraps body content in Jekyll raw tags to prevent Liquid parser crashes."""
    if not content.startswith("---"):
        if "{% raw %}" not in content:
            return "{% raw %}\n" + content + "\n{% endraw %}"
        return content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return content

    front_matter = f"---{parts[1]}---"
    body = parts[2]

    if "{% raw %}" not in body:
        body = f"\n{{% raw %}}\n{body}\n{{% endraw %}}\n"

    return front_matter + body

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        original_content = f.read()

    content = sanitize_front_matter(original_content)
    
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            front_matter = f"---{parts[1]}---"
            body = parts[2]
            body = convert_wikilinks(body, file_path)
            body = convert_callouts(body)
            content = front_matter + body
    else:
        content = convert_wikilinks(content, file_path)
        content = convert_callouts(content)

    # Wrap in raw tags to protect formulas, math, and curly braces from Jekyll
    content = wrap_in_raw(content)

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Sanitized and protected: {file_path}")

def main():
    if not os.path.exists(NOTES_DIR):
        print(f"Directory {NOTES_DIR} not found. Skipping note sanitization.")
        return

    print("Building note map...")
    build_note_map()

    for root, _, files in os.walk(NOTES_DIR):
        for file in files:
            if file.endswith(".md"):
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    main()