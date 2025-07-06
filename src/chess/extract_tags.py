#!/usr/bin/env -S uv run --script
#
# script dependencies added like: uv add --script extract_tags.py "python-chess"
# script originally written by gpt4o, since this is a simple task.
# it only made one small error; the rest I kept as-is.
#
# usage: ./extract_tags.py .../lichess_elite_database > game_tags.jsonl
#
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "python-chess",
# ]
# ///

import sys
import json
from pathlib import Path
import chess.pgn


def extract_tags_from_pgn(pgn_path):
    with open(pgn_path, "r", encoding="utf-8") as pgn_file:
        while True:
            game = chess.pgn.read_game(pgn_file)
            if game is None:
                break
            print(json.dumps(dict(game.headers)))


def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_pgn_tags.py <path_to_directory>")
        sys.exit(1)

    directory = Path(sys.argv[1])
    if not directory.is_dir():
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)

    for pgn_file in directory.glob("*.pgn"):
        extract_tags_from_pgn(pgn_file)


if __name__ == "__main__":
    main()
