"""
Python Study Notes — Modules, Imports, and __name__ == "__main__" (Deep Explanation)

This file explains:
- What importing really means
- Why code runs on import
- What __name__ is and how Python sets it
- WHEN you should use `if __name__ == "__main__"`
- WHEN you should NOT
- The industry-standard mental model for files

Read this slowly once. Then use it as reference.
"""

# ============================================================
# 1) Two kinds of Python files (THIS IS THE KEY IDEA)
# ============================================================

"""
Every Python file you write falls into ONE of these categories:

1) SCRIPT FILE (entry point)
2) MODULE FILE (library / helper)

Confusing these two is the root of most beginner import bugs.
"""

# ------------------------------------------------------------
# SCRIPT FILE (entry point)
# ------------------------------------------------------------

"""
A SCRIPT file is meant to be RUN directly.

Examples:
- main.py
- app.py
- run.py
- migrate.py
- analyze_data.py

You run these like:
    python main.py

Characteristics of a script file:
- It performs actions
- It starts the program
- It may read input, print output, or run logic

SCRIPT FILES SHOULD:
- Contain a main() function
- Use `if __name__ == "__main__":` to start execution
"""

# ------------------------------------------------------------
# MODULE FILE (library / helper)
# ------------------------------------------------------------

"""
A MODULE file is meant to be IMPORTED.

Examples:
- helpers.py
- math_utils.py
- grading.py
- validation.py

You use these like:
    import helpers
    from grading import calculate_grade

Characteristics of a module file:
- It defines functions, classes, constants
- It should NOT perform actions on import
- It should NOT print, ask for input, or run logic automatically

MODULE FILES SHOULD:
- Only define things
- Be safe to import anywhere
"""

# ============================================================
# 2) What REALLY happens when you import a file
# ============================================================

"""
When Python sees:
    import helper

Python does ALL of the following:

1) Finds helper.py
2) Creates a module object named "helper"
3) EXECUTES helper.py top-to-bottom
4) Stores the module in sys.modules
5) Makes it available as the name `helper`

IMPORTANT:
- Importing a file DOES execute its top-level code
- Function definitions are safe (they do not run)
- Print/input/logic at top-level WILL run
"""

# ============================================================
# 3) Example: BAD module design (do NOT do this)
# ============================================================

"""
File: helper.py
"""


# helper.py (BAD)
def greet(name: str) -> None:
    print(f"Hello, {name}")


print("This runs on import!")  # BAD: side effect


"""
File: main.py
"""

# main.py
import helper

"""
Output when running main.py:
This runs on import!

Why this is bad:
- Importing caused unexpected behavior
- Code ran without you explicitly calling it
- This breaks assumptions in large projects
"""

# ============================================================
# 4) __name__: what it is and how Python sets it
# ============================================================

"""
Every Python file has a variable called __name__.

Python sets it automatically.

CASE 1: File is run directly
--------------------------------
Command:
    python helper.py

Inside helper.py:
    __name__ == "__main__"

CASE 2: File is imported
--------------------------------
Code:
    import helper

Inside helper.py:
    __name__ == "helper"

This is NOT magic.
It is Python telling the file:
- "You are the entry point" OR
- "You are being used by another file"
"""

# ============================================================
# 5) The __name__ == "__main__" guard (WHAT IT REALLY DOES)
# ============================================================

"""
The guard:

    if __name__ == "__main__":

means:

"Only run this code IF this file is the program entry point."

It PREVENTS code from running when the file is imported.
"""

# ============================================================
# 6) Correct, industry-standard module design
# ============================================================

"""
File: helper.py
"""


# helper.py (GOOD)
def greet(name: str) -> None:
    print(f"Hello, {name}")


def main() -> None:
    print("helper.py running directly")
    greet("Direct run")


if __name__ == "__main__":
    main()


"""
Behavior:

Run directly:
    python helper.py

Output:
    helper.py running directly
    Hello, Direct run

Imported:
    import helper

Output:
    (nothing)

BUT you can still do:
    helper.greet("Ray")

This is EXACTLY what you want.
"""

# ============================================================
# 7) Answer to the critical question (explicit)
# ============================================================

"""
Question:
"If a module has `if __name__ == "__main__"` and I import it,
will it not run automatically, but I can still use its functions?"

Answer:
YES. Exactly.

- Guarded code does NOT run on import
- Functions and classes ARE defined
- You can freely call them from the importing file
"""

# ============================================================
# 8) Should you add __name__ == "__main__" to EVERY file?
# ============================================================

"""
NO. This is a very important refinement.

Correct rule:

DO NOT ask:
"Should every file have __name__ == '__main__'?"

INSTEAD ask:
"Does this file contain executable logic?"

If YES:
- Add the guard

If NO:
- Do not add it
- There is nothing to guard
"""

# ============================================================
# 9) Examples of when to use the guard
# ============================================================

"""
USE the guard when:
- The file can be run directly
- The file has demo/test logic
- The file has input/output code

Example:
- main.py
- grading.py (with test code)
"""

# ============================================================
# 10) Examples of when NOT to use the guard
# ============================================================

"""
DO NOT use the guard when:
- The file only defines functions/classes
- There is no top-level logic

Example:
"""


# math_utils.py
def add(a: int, b: int) -> int:
    return a + b


def sub(a: int, b: int) -> int:
    return a - b


"""
Nothing runs on import.
No guard needed.
"""

# ============================================================
# 11) Industry-standard rule (memorize this)
# ============================================================

"""
IMPORTS SHOULD DEFINE THINGS, NOT DO THINGS.

- Safe imports
- Predictable behavior
- Fewer bugs
- Easier testing
- Cleaner architecture

This rule scales from small scripts to massive codebases.
"""
