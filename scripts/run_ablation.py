"""Reproduce the segmentation, anchoring, and distance ablation (placeholder)."""

import argparse


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", required=True)
    ap.add_argument("--K", type=int, default=8)
    ap.add_argument("--out", required=True)
    ap.parse_args()
    raise NotImplementedError("Implementation will be released upon acceptance.")


if __name__ == "__main__":
    main()
