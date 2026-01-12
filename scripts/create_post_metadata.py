#!/usr/bin/env python3
import logging
import re
import sys
from pathlib import Path
from collections.abc import Iterator

import yaml

logger = logging.getLogger(__name__)

DATA_DIR = Path("_data")
POSTS_DIR = Path("_posts")


def get_posts() -> Iterator[tuple[Path, dict, str]]:
    for post_file in POSTS_DIR.glob("*.md"):
        with open(post_file, "r") as f:
            content = f.read()
        if content.startswith("---"):
            parts = content.split("---", 2)
            frontmatter = parts[1]
            post = parts[2]
            try:
                front_metadata = yaml.safe_load(frontmatter)
                yield post_file, front_metadata, post
            except Exception as e:
                raise ValueError(f"Failed to read headers for post '{post_file}'.")


def reading_time_minutes(words: int, wpm: int = 200) -> float:
    return words / float(wpm)


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d (%(funcName)s) - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    if not POSTS_DIR.exists():
        raise ValueError(f"Potential configuration error: expected a posts directory at '{POSTS_DIR}'.")
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    n_files_touched = 0
    # TODO compute word count and reading time in _data/post_metadata.yml
    # TODO embed the commit SHAs that touched this file in _data/post_metadata.yml
    
    if n_files_touched > 0:
        logger.error(f"Updated {n_files_touched} file(s).")
        sys.exit(1)
    else:
        logger.info("No file updates to make.")

if __name__ == "__main__":
    main()
