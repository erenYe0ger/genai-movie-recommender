#!/usr/bin/env python3
import os

IGNORE_DIRS = {".venv", "__pycache__", ".pytest_cache", ".git", ".next", "node_modules"}

def tree(path, prefix=""):
    try:
        contents = sorted(os.listdir(path))
    except PermissionError:
        print(prefix + "└── [permission denied]")
        return

    # Filter unwanted entries
    visible_items = []
    for item in contents:
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path) and item in IGNORE_DIRS:
            continue
        visible_items.append(item)

    contents = visible_items

    # If nothing left after filtering
    if not contents:
        print(prefix + "└── (empty)")
        return

    for i, item in enumerate(contents):
        full_path = os.path.join(path, item)
        connector = "└── " if i == len(contents) - 1 else "├── "
        print(prefix + connector + item)

        if os.path.isdir(full_path):
            next_prefix = prefix + ("    " if i == len(contents) - 1 else "│   ")
            tree(full_path, next_prefix)

def main():
    root = os.getcwd()   # Use current directory
    print(root)
    tree(root)

if __name__ == "__main__":
    main()
