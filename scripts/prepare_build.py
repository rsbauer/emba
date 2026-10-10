import os
import shutil
import re
import unicodedata

SOURCE_DIR = "."
BUILD_DIR = "_build_root"
NOTES_SUBDIR = "010 Notes"

def slugify(value):
    """Converts a string or path segment into a lowercase, URL-friendly slug."""
    value = str(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = value.replace('&', 'and')
    value = re.sub(r'[^\w\s\-/]', '', value)
    value = re.sub(r'[-\s]+', '-', value).strip('-')
    return value.lower()

def build_staging():
    """Creates a temporary staging directory containing a copy of the repo."""
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
    
    ignore_list = {'.git', '_site', BUILD_DIR, '.github', 'scripts'}
    shutil.copytree(SOURCE_DIR, BUILD_DIR, ignore=shutil.ignore_patterns(*ignore_list))

def rename_in_staging():
    """Recursively slugifies file and folder names ONLY in the staging directory."""
    notes_build_path = os.path.join(BUILD_DIR, NOTES_SUBDIR)
    if not os.path.exists(notes_build_path):
        return

    for root, dirs, files in os.walk(notes_build_path, topdown=False):
        for file in files:
            if file.endswith(".md"):
                old_path = os.path.join(root, file)
                name, ext = os.path.splitext(file)
                new_file = slugify(name) + ext
                new_path = os.path.join(root, new_file)
                if old_path != new_path:
                    os.rename(old_path, new_path)

        for d in dirs:
            old_dir_path = os.path.join(root, d)
            new_dir_name = slugify(d)
            new_dir_path = os.path.join(root, new_dir_name)
            if old_dir_path != new_dir_path:
                os.rename(old_dir_path, new_dir_path)

def convert_obsidian_math(body):
    """ Converts Obsidian single-dollar inline math ($...$) to Kramdown/MathJax compatible \(_...\) """
    # This regex matches single-dollar inline math while avoiding block math ($$...$$)
    # It ensures there are no spaces immediately inside the dollar signs
    inline_math_pattern = re.compile(r'(?<!\$)\$(?!\s)([^$\n]+?)(?<!\s)\$(?!\$)')
    return inline_math_pattern.sub(r'\\(\1\\)', body)

def process_staging_notes():
    """Processes front matter, wikilinks, callouts, and math delimiters."""
    notes_build_path = os.path.join(BUILD_DIR, NOTES_SUBDIR)
    if not os.path.exists(notes_build_path):
        return

    slug_map = {}
    for root, _, files in os.walk(notes_build_path):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, start=BUILD_DIR).replace("\\", "/")
                base_name = os.path.splitext(file)[0].lower()
                slug_map[base_name] = rel_path

    for root, _, files in os.walk(notes_build_path):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                if not content.startswith("---"):
                    content = "---\nlayout: default\nrender_with_liquid: false\n---\n" + content

                parts = content.split("---", 2)
                if len(parts) >= 3:
                    fm = parts[1]
                    body = parts[2]
                    
                    lines = fm.splitlines()
                    fixed_fm = []
                    has_liquid_setting = False
                    
                    for line in lines:
                        if line.startswith("title:") and ":" in line[6:]:
                            _, val = line.split(":", 1)
                            val = val.strip()
                            if not (val.startswith('"') and val.endswith('"')):
                                val_escaped = val.replace('"', '\\"')
                                line = f'title: "{val_escaped}"'
                        if "render_with_liquid" in line:
                            has_liquid_setting = True
                        fixed_fm.append(line)

                    if not has_liquid_setting:
                        fixed_fm.append("render_with_liquid: false")

                    fm = "\n".join(fixed_fm)

                    # 1. Convert Obsidian Inline Math to MathJax-safe format
                    body = convert_obsidian_math(body)

                    # 2. Convert Wikilinks
                    def replace_wikilink(match):
                        target = match.group(1).strip()
                        label = match.group(2).strip() if match.lastindex >= 2 and match.group(2) else target
                        lookup = os.path.basename(target).lower()
                        if lookup.endswith(".md"):
                            lookup = lookup[:-3]
                        if lookup in slug_map:
                            target_rel = slug_map[lookup]
                            current_dir = os.path.dirname(os.path.relpath(file_path, start=BUILD_DIR)).replace("\\", "/")
                            rel_link = os.path.relpath(target_rel, start=current_dir).replace("\\", "/")
                            return f'[{label}]({rel_link})'
                        return f'[{label}]({slugify(target)}.md)'

                    body = re.sub(r'\[\[([^|\]]+)(?:\|([^\]]+))?\]\]', replace_wikilink, body)

                    # 3. Convert Callouts
                    body = re.sub(r'>\s*\[!(\w+)\](?:\s+(.*))?', r'> **\2**', body)

                    content = f"---{fm}---{body}"

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)

if __name__ == "__main__":
    print("Creating staging build directory...")
    build_staging()
    print("Slugifying files and folders in staging...")
    rename_in_staging()
    print("Processing notes content and normalizing math in staging...")
    process_staging_notes()
    print("Staging preparation complete.")