import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Count lines, words, and characters.")
    parser.add_argument("file", type=Path, help="A UTF-8 text file.")
    args = parser.parse_args()

    try:
        content = args.file.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        parser.error(str(error))

    counts = {
        "lines": len(content.splitlines()),
        "words": len(content.split()),
        "characters": len(content),
    }
    print(json.dumps(counts))


if __name__ == "__main__":
    main()