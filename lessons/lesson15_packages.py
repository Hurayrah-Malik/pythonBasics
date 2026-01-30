"""
============================================================
__init__.py — WHAT IT IS, WHAT IT DOES, AND WHY IT EXISTS
============================================================

What __init__.py is:
-------------------
- __init__.py is a NORMAL Python file.
- It has no special syntax.
- What’s special is *when* it runs.

When it runs:
-------------
When you do:
    import mypackage

Python:
1) Finds the folder `mypackage/`
2) Executes `mypackage/__init__.py` ONCE
3) Creates the package object
4) Makes it available as `mypackage`

So:
- __init__.py runs at *package import time*
- Not at program start
- Not per file inside the package

Why it is called __init__.py:
-----------------------------
Same idea as a class initializer:

    class MyClass:
        def __init__(self):
            ...

- Class __init__ → initializes an instance
- Package __init__.py → initializes a package

Same concept, different level.

What code goes in __init__.py:
------------------------------

1) NOTHING (MOST COMMON)
   ---------------------
   An empty file:

       # mypackage/__init__.py

   Purpose:
   - Explicitly marks the folder as a package
   - Works in all Python versions and tools
   - Industry standard

2) RE-EXPORTING FUNCTIONS (COMMON)
   -------------------------------
       from .parser import parse_csv
       from .utils import clean_row

   Allows:
       import mypackage
       mypackage.parse_csv()

   Instead of:
       mypackage.parser.parse_csv()

   This defines the *public API* of the package.

3) PACKAGE-LEVEL CONSTANTS
   -----------------------
       VERSION = "1.0.0"

4) LIGHT SETUP (USE CAREFULLY)
   ---------------------------
       print("mypackage loaded")

   This runs ONCE when imported.
   Avoid side effects here.

What should NOT go in __init__.py:
----------------------------------
- Heavy computation
- File I/O
- Network calls
- Program logic
- Anything you wouldn’t want to run during import

Rule:
-----
Importing a package should be:
- Fast
- Safe
- Side-effect free

Do you need __init__.py?
-----------------------
- Python 3.3+ allows packages without it (namespace packages)
- BUT industry practice is still to include it

Recommended rule:
-----------------
ALWAYS add __init__.py to folders meant to be packages.
Even if it’s empty.

Summary:
--------
- __init__.py is a normal Python file
- Runs once when the package is imported
- Initializes the package namespace
- Often empty
- Used to define a package’s public interface

============================================================
"""
