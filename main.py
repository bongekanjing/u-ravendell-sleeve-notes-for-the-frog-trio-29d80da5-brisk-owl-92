#!/usr/bin/env python3
"""Write the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output)."""
import os

TEXT = """Low Water

The pianist plays like the ceiling is leaking and has decided not to mention it. The bassist counts in under his breath all night. On "Heron" the drummer lays out for four bars and you can hear the pond deciding something. Recorded live in a boathouse, two mics, no overdubs."""


def validate():
    if not TEXT.strip():
        raise SystemExit("TEXT is blank or only whitespace")
    if len(TEXT) > 400:
        raise SystemExit("TEXT is longer than 400 characters (%d)" % len(TEXT))


def main():
    validate()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(TEXT)
    with open(target, "rb") as handle:
        written = handle.read()
    if written != TEXT.encode("utf-8"):
        raise SystemExit("readback mismatch for %s" % target)
    print(target)


if __name__ == "__main__":
    main()
