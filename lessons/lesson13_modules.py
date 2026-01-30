"""
Python Study Notes — Modules (imports, sys.modules, __name__ == "__main__")

Short explanations. Examples include expected outputs.


Core ideas:
- A module is a .py file.
- Importing a module executes its top-level code exactly once per process.
- sys.modules is a runtime cache (a dict) of already-imported modules.
- __name__ tells you whether a file is running as a script or being imported.
- Package = folder of modules. Library = collection of packages.
"""

# ============================================================
# 0) Vocabulary: module vs package vs library (and where classes fit)
# ============================================================

"""
Module:
- A single Python file: something.py

Package:
- A directory (folder) that groups modules:
  mypkg/
    __init__.py   (optional in modern Python, but common)
    a.py
    b.py

Library:
- A collection of packages/modules distributed together (often installed via pip).
  Example: "requests" is a library (it contains packages/modules).

Where do classes fit?
- Classes are defined INSIDE modules (modules are where code lives).
- Structure is typically:
  library -> packages -> modules -> (functions/classes/constants)
"""


# ============================================================
# 1) sys.modules: what it is (and what it is NOT)
# ============================================================

"""
Your note: "sys.modules. what location is that in? Is it in the root folder?"

Answer:
- sys.modules is NOT a folder and not a location on disk.
- sys.modules is a *dictionary in memory* (runtime cache) mapping:
    module_name (str) -> module object
- It exists in the running Python process.
- It’s how Python avoids re-importing the same module repeatedly.
"""

import sys

print(type(sys.modules))  # <class 'dict'>  (runtime object, not a directory)
# Example: show a few keys (module names) already loaded by Python
print(list(sys.modules)[:5])  # output varies by environment


# ============================================================
# 2) Import executes top-level module code immediately
# ============================================================

"""
Your note: "When module is imported, all of the code inside is executed immediately."

Precise version:
- When you import a module, Python:
  1) finds the module
  2) creates a module object
  3) EXECUTES the module file top-to-bottom (top-level statements)
  4) stores it in sys.modules
- After that, importing again reuses the cached module from sys.modules,
  so top-level code is NOT executed again in the same process.


"""

# NOTE: The following is "multi-file" behavior. You would create these files:
#
# one.py
#   def hello(): print("one hello")
#   print("one")
#
# two.py
#   import three
#   def hello(): print("two hello"); three.hello()
#   print("two")
#
# three.py
#   def hello(): print("three hello")
#   print("three")
#
# main.py
#   import one, two, three
#   one.hello()
#   two.hello()
#   three.hello()

"""
Expected behavior (conceptual):
- When main.py imports one, two, three:
  - The top-level prints in each module run DURING import.

Important detail:
- Import order + nested imports matters.
- If two.py imports three.py, and main.py also imports three.py:
  - three.py executes only once, because it’s cached in sys.modules.
"""


# ============================================================
# 3) Aliasing: rename a module or a function at import time
# ============================================================

"""
Your note: "You can also rename the module being imported to something else,
even functions can be renamed."

Module alias:
    import math as m

Function alias:
    from math import sqrt as root

This is just name-binding:
- "as" creates a new name in YOUR file that points to the imported object.
"""

import math as m
from math import sqrt as root

print(m.pi)  # 3.141592653589793
print(root(9))  # 3.0


# ============================================================
# 4) __name__ == "__main__": script vs imported module
# ============================================================

"""
============================================================
__name__ == "__main__" — FULL EXPLANATION (NOTES)
============================================================

Core fact:
----------
Every Python file is a *module*. When Python loads a module, it automatically
sets a global variable called:

    __name__

What value __name__ gets depends on *how* the file is used.

------------------------------------------------------------
CASE 1: File is run directly (as a script)
------------------------------------------------------------

Command:
    python mainFile.py

Python sets:
    __name__ = "__main__"

So this condition is TRUE:
    if __name__ == "__main__":

Meaning:
- This file is the program entry point
- Code inside the guard should run automatically

Example:
    def main():
        print("program logic")

    if __name__ == "__main__":
        main()     # runs automatically when file is executed

------------------------------------------------------------
CASE 2: File is imported (as a module)
------------------------------------------------------------

Code:
    import mainFile

Python sets:
    __name__ = "mainFile"

So this condition is FALSE:
    if __name__ == "__main__":

Meaning:
- The file is being used by another file
- Guarded code does NOT run automatically

IMPORTANT:
- The file is still imported
- All functions and variables are defined
- Nothing inside the guard executes

------------------------------------------------------------
WHY YOU CAN STILL CALL mainFile.main()
------------------------------------------------------------

The guard does NOT:
- prevent importing
- hide functions
- block function calls

It ONLY prevents *automatic execution at import time*.

Example:
    import mainFile
    mainFile.main()   # this WILL run

This is intentional.
If you explicitly call a function, Python assumes you meant to.

------------------------------------------------------------
WHAT PROBLEM THIS SOLVES
------------------------------------------------------------

Without the guard:

    print("program logic")

This would run:
- when the file is executed
- when the file is imported   ❌ (bad side effect)

With the guard:
- Runs only when intended
- Imports stay clean and safe

------------------------------------------------------------
PROFESSIONAL RULE
------------------------------------------------------------

- Any file with program flow, I/O, or execution logic:
      USE if __name__ == "__main__"

- Helper / utility modules:
      Optional, but still acceptable

------------------------------------------------------------
ONE-SENTENCE SUMMARY
------------------------------------------------------------

(if __name__ == "__main__") does NOT stop imports —
it stops code from running automatically when a file is imported.

============================================================
"""


# Multi-file example matching your lecture screenshot:
#
# module.py
#   length = 10
#   width = 20
#   print("Running as imported module")
#
#   if __name__ == "__main__":
#       print("Running as a script")
#       print(f"Module length = {length}")
#       print(f"Module width = {width}")
#
# main.py
#   import module
#
#   length = 1
#   width = 2
#
#   print("Script values")
#   print(f"Length = {length}")
#   print(f"Width = {width}")
#
#   print("Module values")
#   print(f"Length = {module.length}")
#   print(f"Width = {module.width}")

"""
What happens when you RUN main.py:
- main.py starts executing.
- It hits: import module
  -> module.py executes top-level code:
     prints: "Running as imported module"
  -> module.__name__ is "module" (NOT "__main__"), so the guarded block does NOT run.
- Then main.py continues and prints its script/module values.

Key beginner rule:
- A module’s variables live in its own namespace.
- main.py's `length` is different from module.py's `length`.
- You access module variables via: module.length, module.width
"""


# ============================================================
# 5) Beginner footguns (short, high-value)
# ============================================================

"""
Footgun A: Top-level code runs on import
- If you put input() / print() / file writes at top-level in a module,
  importing it will trigger those effects immediately.
Fix:
- Put runnable code behind:
    if __name__ == "__main__":


"""

"""
============================================================
IMPORTING FUNCTIONS FROM MODULES — HOW IT REALLY WORKS
============================================================

Scenario:
---------
You have two files:

    mainFile.py
    moduleOne.py

`moduleOne.py` contains a function:

    def hello():
        print("hello")

------------------------------------------------------------
CASE 1: Standard import (MOST COMMON / RECOMMENDED)
------------------------------------------------------------

In mainFile.py:
    import moduleOne

How to call the function:
    moduleOne.hello()

Why this works:
- The entire module is imported
- `hello` lives inside the `moduleOne` namespace
- You must qualify it with `moduleOne.`

Why this is good practice:
- Very explicit
- Avoids name collisions
- Makes it obvious where functions come from
- Most common in professional codebases

------------------------------------------------------------
CASE 2: Import the function directly
------------------------------------------------------------

In mainFile.py:
    from moduleOne import hello

How to call the function:
    hello()

What this does:
- Copies `hello` into the current file’s namespace
- You no longer need `moduleOne.`

Tradeoff:
- Shorter
- But easier to accidentally shadow names
- Slightly less explicit

------------------------------------------------------------
CASE 3: Import everything (DO NOT USE)
------------------------------------------------------------

In mainFile.py:
    from moduleOne import *

How to call the function:
    hello()

Why this is bad:
- You don’t know where names come from
- Easy to overwrite variables
- Makes code harder to read and debug
- Generally rejected in industry code

------------------------------------------------------------
IMPORTANT RULE (VERY IMPORTANT)
------------------------------------------------------------

You CANNOT do this:
    hello()

Unless you explicitly imported `hello` into the file.

This WILL NOT work:
    import moduleOne
    hello()          # NameError

This WILL work:
    import moduleOne
    moduleOne.hello()

------------------------------------------------------------
RULE OF THUMB
------------------------------------------------------------

- Default choice:
      import moduleOne
      moduleOne.hello()

- Acceptable for small, stable helpers:
      from moduleOne import hello

- Never:
      from moduleOne import *

------------------------------------------------------------
ONE-SENTENCE SUMMARY
------------------------------------------------------------

Functions live inside their module’s namespace unless you explicitly
import them into the current file.

============================================================
"""
