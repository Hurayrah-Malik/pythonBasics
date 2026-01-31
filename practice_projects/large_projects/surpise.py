"""
random_surprise.py

What it does (high level):
- Simulates a tiny "system" that watches you.
- Uses randomness, time, and harmless tricks.
- Produces different behavior on each run.

No input required.
Safe to run.
"""

import random
import time
import sys
from datetime import datetime


def type_out(text: str, delay: float = 0.03) -> None:
    """Print text one character at a time."""
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()


def fake_analysis() -> None:
    steps = [
        "Scanning environment",
        "Collecting entropy",
        "Evaluating probabilities",
        "Predicting outcomes",
        "Finalizing decision",
    ]
    for step in steps:
        dots = "." * random.randint(1, 5)
        print(f"{step}{dots}")
        time.sleep(random.uniform(0.3, 0.8))


def fortune() -> str:
    fortunes = [
        "You will debug something today that wasn't actually broken.",
        "Your next error will be caused by a single character.",
        "You will overthink a problem that needed a loop.",
        "A print statement will save you.",
        "The bug will disappear when someone watches.",
    ]
    return random.choice(fortunes)


def glitch() -> None:
    for _ in range(3):
        line = "".join(random.choice("01#@$%&*") for _ in range(random.randint(20, 40)))
        print(line)
        time.sleep(0.05)


def main() -> None:
    type_out("Initializing…")
    fake_analysis()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\nTimestamp locked: {now}")

    decision = random.random()

    if decision < 0.4:
        type_out("\nOutcome: OBSERVATION MODE")
        type_out("You are being watched by absolutely nothing.")
        glitch()

    elif decision < 0.8:
        type_out("\nOutcome: PREDICTION MODE")
        type_out("System prediction:")
        time.sleep(0.5)
        print(f"→ {fortune()}")

    else:
        type_out("\nOutcome: TERMINATION MODE")
        type_out("Nothing dramatic will happen.")
        time.sleep(0.5)
        type_out("This message was unnecessary.")

    print("\nExit code:", random.choice([0, 0, 0, 1]))
    sys.exit(0)


if __name__ == "__main__":
    main()
