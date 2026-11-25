"""Fix Human Sleep: Funniest Patch Note — make.fun bounty entry.

Competition: u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27
($2, winner-takes-all; deadline 26 Nov 2026 23:10 WIB).
Judge: z-ai/glm-5.3-flash, pairwise, no ties. Criteria in order:
(1) really a patch note about fixing human sleep, (2) the joke,
(3) the changelog voice, (4) fit to a single line.
Gate: entry.txt must be UTF-8 text of 1 to 160 characters, single line.

Candidate draft table (scored 1-5: patch-note-about-sleep / joke /
changelog-voice / single-line-fit; total out of 20):

1. "Fixed a bug where humans woke up at 3 a.m. to replay a conversation
   from 2019. Sleep now ships with a mute button for your own brain."
   5/5/5/5 = 20  <-- WINNER
2. "Patch 1.0.1: Fixed a bug where the snooze button filed for overtime.
   Sleep now starts on time; snooze is now a formal complaint form."
   5/4/5/5 = 19
3. "Fixed a bug where REM cycles shipped without release notes. Dreams now
   include a changelog; nightmares are listed under Known Issues."
   5/4/5/5 = 19
4. "Fixed a bug where the brain replayed every embarrassing moment at
   3 a.m. Sleep now runs clean; side effect: you may miss your regrets."
   5/4/5/5 = 19
5. "Fixed a bug where humans treated 2 a.m. as thinking time. Sleep now
   locks the brain group chat until morning; unread messages: 0."
   5/4/5/5 = 19
6. "Changelog: Fixed a bug where sleep paused whenever the brain remembered
   something awkward from 2014. Cringe playback is now disabled."
   5/4/5/5 = 19
7. "Fixed a bug where the body woke up before the alarm to worry about the
   alarm. Sleep now runs until the alarm; pre-alarm anxiety deprecated."
   5/4/5/5 = 19
8. "Patch 1.0: Fixed a bug where dreams buffered at the best part. Sleep
   now streams in full; the 3 a.m. dread update has been rolled back."
   5/4/5/5 = 19
9. "Fixed a bug where humans woke up refreshed only on days with nowhere
   to be. Sleep now works on weekdays too; weekends remain in beta."
   5/4/4/5 = 18

Winner rationale: candidate 1 is the only one scoring a perfect 20.
It opens in classic changelog voice ("Fixed a bug where..."), names the
most specific, relatable sleep bug in the field (the 3 a.m. replay of a
years-old conversation — fresher than the crowded "woke up tired" /
"dreams take longer to load" lines), and lands the punch in the second
clause with a changelog-plausible fix ("ships with a mute button") that
is absurd when applied to your own brain. 133 characters, single line.
"""

import os
import sys

LINE = (
    "Fixed a bug where humans woke up at 3 a.m. to replay a conversation "
    "from 2019. Sleep now ships with a mute button for your own brain."
)

MAX_CHARS = 160


def main() -> int:
    if not LINE.strip():
        print("error: LINE is empty", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: LINE must be exactly one line (no newline characters)", file=sys.stderr)
        return 1
    if len(LINE) > MAX_CHARS:
        print(
            "error: LINE is %d characters, over the %d limit"
            % (len(LINE), MAX_CHARS),
            file=sys.stderr,
        )
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE + "\n":
        print("error: entry.txt does not match LINE exactly", file=sys.stderr)
        return 1

    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
