# Warning Label for Humans entry: one funny line, written to /output/entry.txt.
# Standard library only, no network. The bytes are identical on every run.
# The line: a real printed-label warning ("WARNING: This human will ...")
# about the most universal human trait -- ignoring instructions -- with
# the turn landing in the last few words ("the exact opposite of what
# it says"). The label warns about itself being skimmed, which is the
# joke: recognition first, then the punch, in one idea, no filler.
import os

LINE = "WARNING: This human will ignore every instruction, skim this label, and confidently do the exact opposite of what it says."

OUTPUT_PATH = "/output/entry.txt"

assert 1 <= len(LINE) <= 160, "entry must be 1 to 160 characters"
assert LINE.strip() == LINE and LINE.strip(), "entry must not be only whitespace"

# Gate check the way the sealed scorer measures it: decode the UTF-8
# bytes back and count characters, not bytes.
text = LINE.encode("utf-8").decode("utf-8")
assert 1 <= len(text) <= 160, "entry must be 1 to 160 characters"
assert text.strip(), "entry must not be only whitespace"

os.makedirs("/output", exist_ok=True)
# No trailing newline: the file holds exactly the line, nothing else.
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(LINE)

# Read the file back and confirm it holds exactly the line: the sealed
# scorer reads the bytes we wrote, so the write itself must round-trip.
with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
    written = handle.read()
assert written == LINE, "written entry must equal the line exactly"
assert 1 <= len(written) <= 160, "written entry must be 1 to 160 characters"
