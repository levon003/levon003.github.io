#!/usr/bin/env python3
import logging
import re
import sys
from pathlib import Path

import yaml

logger = logging.getLogger(__name__)

TAGS_DIR = Path("tags")
POSTS_DIR = Path("_posts")


def get_tags() -> set[str]:
    tags = set()
    for post_file in POSTS_DIR.glob("*.md"):
        with open(post_file, "r") as f:
            content = f.read()
        if content.startswith("---"):
            frontmatter = content.split("---", 2)[1]
            try:
                data = yaml.safe_load(frontmatter)
                if "tags" in data:
                    if isinstance(data["tags"], str):
                        tags.update(data["tags"].split())
                    else:
                        tags.update(data["tags"])
            except Exception as e:
                raise ValueError(f"Failed to read headers for post '{post_file}'.")
    return tags


def slugify(tag):
        # Jekyll-like slugify, per ChatGPT
        tag = tag.lower()
        tag = re.sub(r"[^a-z0-9\s-]", "", tag)
        tag = re.sub(r"\s+", "-", tag)
        tag = re.sub(r"-+", "-", tag)
        return tag.strip("-")

def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d (%(funcName)s) - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    if not POSTS_DIR.exists():
        raise ValueError(f"Potential configuration error: expected a posts directory at '{POSTS_DIR}'.")
    TAGS_DIR.mkdir(parents=True, exist_ok=True)

    tags = get_tags()

    # Write a page per tag
    new_tags = set()
    for tag in sorted(tags):
        slug = slugify(tag)
        filename = TAGS_DIR / f"{slug}.md"
        if not filename.exists():
            with open(filename, "w") as f:
                f.write(f"""---
layout: tag
tag: {tag}
permalink: /tags/{slug}/
---
""")
            logger.info(f"Created tag stub '{filename}'.")
            new_tags.add(tag)
    
    if len(new_tags) > 0:
        logger.error(f"Created {len(new_tags)} new tag(s).")
        sys.exit(1)
    else:
        logger.info("No new tag stubs created.")

if __name__ == "__main__":
    main()
