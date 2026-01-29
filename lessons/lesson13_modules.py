"""
Python Study Notes — Modules (imports, sys.modules, __name__ == "__main__")

Short explanations. Examples include expected outputs.

Based on lecture notes in: CS 2 notes.pdf :contentReference[oaicite:0]{index=0}

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

This matches the image on page 1: importing one/two/three causes their top-level
print statements to run. :contentReference[oaicite:1]{index=1}
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
Your note (page 2):
- If a file has `if __name__ == "__main__":`, it's a hint it's designed to run as a script.
- If it doesn't, it's a hint it's meant to be imported as a module.

Precise model:
- Every module has a global variable named __name__.
- If the file is RUN directly:      __name__ == "__main__"
- If the file is IMPORTED:          __name__ == "module_name"

This matches the screenshot on page 1 with main.py and module.py. :contentReference[oaicite:2]{index=2}
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

Footgun B: Circular imports
- Example: a imports b, and b imports a.
- Often caused by top-level imports + top-level execution that depends on each other.
Fix:
- Move imports inside functions (when appropriate)
- Refactor shared code into a third module

Footgun C: "from module import name" copies a reference at import time
- If module.name later changes, your imported name might not reflect it.
- Prefer: import module; use module.name
"""


# ============================================================
# 6) Micro-exercises (quick checks)
# ============================================================

"""
Exercise 1:
- Create a file helpers.py with: print("helpers loaded")
- In main.py, import helpers twice.
Question:
- How many times does "helpers loaded" print, and why? (sys.modules)

Exercise 2:
- In helpers.py, add:
    if __name__ == "__main__":
        print("helpers running as script")
- Run helpers.py directly vs import it.
Question:
- Which lines print in each case, and why? (__name__)
"""
