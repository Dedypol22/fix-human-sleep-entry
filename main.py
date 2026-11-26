"""Fix Human Sleep: Funniest Patch Note (R2) — one-line patch-note entry.

Winning line:
    Fixed a bug where sleep installed updates at 3 a.m. and restarted the human without warning.

Why it wins:
    - Fresh angle: maps the universal nightmare of a forced OS update restart
      (no warning, 3 a.m.) onto sleep — a joke family the field has not flooded.
    - Pure changelog voice: "Fixed a bug where ...", one clause, no filler.
    - One instantly visual punch: sleep as an updater that restarts the human.
    - 92 characters, a single line — comfortably inside the 1-160 gate.

Candidate scoring (1-5 per criterion: patch-note-about-sleep / joke /
changelog voice / single-line fit). #0 is the standing R1 line (rank 443/1641,
score 552535); #1 is the winner, the only 20 and the only joke score of 5.

    #  C1 C2 C3 C4  Total  Candidate
    0  5  4  4  5   18     3 a.m. replay 2019 + mute button for your own brain (R1)
    1  5  5  5  5   20     WINNER: sleep installed updates at 3 a.m., restarted the human without warning
    2  5  4  5  5   19     Woke up five minutes before the alarm; the alarm now respects the contract
    3  5  4  5  5   19     Sleep auto-saves every 90 minutes; unsaved dreams lost if you wake mid-REM
    4  5  4  5  5   19     Snooze button files a formal complaint after the third press
    5  5  4  5  5   19     Brain treated bedtime as a suggestion; bedtime now enforced, no appeals
    6  5  4  5  5   19     Brain ran a full systems check at 2 a.m.; updates scheduled for never
    7  5  4  5  5   19     Alarm snoozed itself; reminded who is in charge
    8  5  4  4  5   18     47 browser tabs open in your brain; tabs close at bedtime
    9  5  4  5  4   18     Dreams about work emails had no unsubscribe link; nightmares now include one
    10 5  3  5  5   18     Known issue: dreams may buffer during heavy REM; fix scheduled for next nap
    11 5  4  4  5   18     Patch 2.0: airplane mode for your brain; overthinking grounded (R1 derivative)
    12 4  3  5  5   17     Snoring ships with a mute toggle; partners may finally install the update
    13 4  4  4  5   17     Fell asleep during movies, woke up at the sequel; sleep pauses at the credits
    14 5  3  4  5   17     Woke up exhausted after nine hours; sleep now saves your progress ("bangun lelah" family — avoided)

The program writes the winning line to entry.txt in MAKEFUN_OUTPUT_DIR
(default /output), with no trailing newline, and verifies the file matches
the line byte for byte.
"""

import os
import sys

LINE = "Fixed a bug where sleep installed updates at 3 a.m. and restarted the human without warning."

MAX_CHARS = 160


def main() -> int:
    """Write LINE to entry.txt and verify it byte for byte. Return 0 or 1."""
    if not LINE:
        print("error: winning line is empty", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: winning line must be a single line", file=sys.stderr)
        return 1
    if len(LINE) > MAX_CHARS:
        print(
            f"error: winning line is {len(LINE)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)

    with open(entry_path, "rb") as handle:
        written = handle.read()
    expected = LINE.encode("utf-8")
    if written != expected:
        print(
            f"error: entry.txt ({len(written)} bytes) does not match the winning "
            f"line ({len(expected)} bytes) byte for byte",
            file=sys.stderr,
        )
        return 1

    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
