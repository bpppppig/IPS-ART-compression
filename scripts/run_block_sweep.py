"""Reproduce the block-size and latency measurements (entry point placeholder)."""

import argparse


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", required=True)
    ap.add_argument("--blocks", default="1,2,4,8,16,32,64,128")
    ap.add_argument("--out", required=True)
    ap.parse_args()
    raise NotImplementedError("Implementation will be released upon acceptance.")


if __name__ == "__main__":
    main()
