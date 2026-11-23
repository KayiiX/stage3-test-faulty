"""Stage 3 test team with two deliberate mistakes (for practising inspection)."""
from .learner import run

# MISTAKE 1: a hard-coded folder instead of the F1TENTH_DATA_DIR variable
DATA = "/home/team/stage3_data"


def main():
    # MISTAKE 2: always loads the saved lap, so it crashes when practice saved nothing
    run(data_dir_override=DATA, crash_without_lap=True)
