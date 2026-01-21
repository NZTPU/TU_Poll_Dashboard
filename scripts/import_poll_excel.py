"""Placeholder script for importing TU polling Excel data."""

import sys


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python scripts/import_poll_excel.py <path-to-excel>")
        raise SystemExit(1)

    excel_path = sys.argv[1]
    print(f"[placeholder] Would import polling data from: {excel_path}")


if __name__ == "__main__":
    main()
