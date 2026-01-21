"""
Truthiness & Boolean Logic (Python) — Study Notes

Core idea:
- `if x:` does NOT mean x == True.
- `if x:` means: "Is x truthy?"

Python converts objects to True/False using truthiness rules.

Two key operator rules (memorize):
- a and b  -> first falsy, else last
- a or b   -> first truthy, else last
"""

# ============================================================
# 1) Truthiness: what counts as False in an if?
# ============================================================

# These are falsy (treated as False in conditionals):
# - False
# - None
# - 0, 0.0
# - "" (empty string)
# - [] (empty list)
# - () (empty tuple)
# - {} (empty dict)
# - set() (empty set)

# Everything else is truthy.

print(bool(False))     # False
print(bool(None))      # False
print(bool(0))         # False
print(bool(0.0))       # False
print(bool(""))        # False
print(bool([]))        # False
print(bool(()))        # False
print(bool({}))        # False
print(bool(set()))     # False

print(bool(1))         # True
print(bool(-1))        # True
print(bool("hi"))      # True
print(bool([0]))       # True  (non-empty list is truthy even if it contains 0)


# ============================================================
# 2) if x: checks truthiness, not equality to True
# ============================================================

x = 2

# Truthiness check:
if x:
    print("x is truthy")   # prints

# Equality check with True:
if x == True:
    print("x == True")     # does NOT print, because 2 == True is False

# Identity check (same object in memory) with True (almost always wrong):
#even if value of x was True, this would still be a false statement:
if x is True:
    print("x is True")     # does NOT print (x is an int object, not the bool True object)

# Key idea:
# - `if x:` asks: "is x truthy?"
# - `if x == True:` asks: "does x equal True?"
# - `if x is True:` asks: "is x literally the True object? (same object in memory)"

# ============================================================
# Identity vs Truthiness with True
# ============================================================

# True is a singleton object in Python
# There is exactly ONE True object in memory

print(True is True)        # True  (same object)


# x is bound directly to the True object
x = True

print(x is True)           # True  (x refers to the same True object)
print(x == True)           # True  (value equality)
print(bool(x))             # True  (truthiness)


# Now compare with a truthy value that is NOT the True object
y = 1

print(y == True)           # True  (1 equals True in value)
print(y is True)           # False (different objects in memory)
print(bool(y))             # True  (truthy)


# Correct usage patterns
if x is True:
    print("x is exactly the True object")   # prints

if y:
    print("y is truthy (but not True)")     # prints

# Incorrect / misleading pattern
if y is True:
    print("This will NOT print")            # never prints


# ============================================================
# 3) Why `if x is True:` is almost always wrong
# ============================================================

# `is` checks identity , not truthiness.
# It is only correct when you truly mean "exactly the True object".

print(True == 1)       # True  (value equality; bool is a subclass of int)
print(True is 1)       # False (identity; different objects)

# Correct usage of `is` in practice:
# - checking against None (None is a singleton object)
value = None
if value is None:
    print("value is None")  # prints


# ============================================================
# 4) and / or return OBJECTS (not necessarily booleans)
# ============================================================

# Everything in Python is an object, including True and False.
# `and` and `or` return one of their operands.

# Rule:
# - a and b -> first falsy, else last (stops at first falsy)
# - a or b  -> first truthy, else last (stops at first truthy)
# From a short-circuit perspective, and and or return the value where evaluation stopped.

print(0 and 5)            # 0        (first falsy is 0, so return 0)
print(3 and 5)            # 5        (3 is truthy, so return last operand)
print([] and "x")         # []       (first falsy is [], so return [])
print("hi" and "bye")     # "bye"    (first is truthy, return last)

print(0 or 5)             # 5        (first truthy is 5)
print(3 or 5)             # 3        (first operand is already truthy, return it)
print([] or "hello")      # "hello"  ([] is falsy, so return "hello")
print("hi" or "bye")      # "hi"     (already truthy, so return it)

# Why this design is useful:
# - it selects useful values without extra if-statements
# - it short-circuits (doesn't evaluate the second operand if not needed)


# ============================================================
# 5) Short-circuiting (prevents errors + avoids wasted work)
# ============================================================

# `and` short-circuits: if left side is falsy, it returns left side and stops.
x = []
# This does NOT crash because x is falsy, so x[0] is never evaluated.
if x and x[0] == 1:
    print("won't print")

# `or` short-circuits: if left side is truthy, it returns left side and stops.
name = "Ray"
result = name or name.strip()  # name is truthy, so right side is never evaluated
print(result)                  # "Ray"

# Common safe pattern:
# guard an operation that would crash if the container is empty
data = []
first = data and data[0]       # returns [] (falsy) instead of crashing
print(first)                   # []


# ============================================================
# 6) Practical idioms (why and/or can be better than if)
# ============================================================

# (A) "Only transform if non-empty"
user_input = "   hello   "
cleaned = user_input and user_input.strip()
print(cleaned)                 # "hello"

user_input = ""
cleaned = user_input and user_input.strip()
print(cleaned)                 # ""  (strip not called)

# Equivalent if-statement:
# if user_input:
#     cleaned = user_input.strip()
# else:
#     cleaned = user_input

# (B) Provide a default value with `or`
user_input = ""
name = user_input or "Anonymous"
print(name)                    # "Anonymous"

user_input = "Aisha"
name = user_input or "Anonymous"
print(name)                    # "Aisha"

# (C) Choose a fallback container
maybe_results = []
results = maybe_results or [1, 2, 3]
print(results)                 # [1, 2, 3]


# ============================================================
# 7) Footguns (easy mistakes that cause bugs)
# ============================================================

# "Footgun" = valid code that is easy to misuse and accidentally create bugs.

# (1) Using `is` for truthiness
x = 1
if x is True:
    print("bad")               # never prints; wrong check for truthiness

# (2) Comparing to True/False instead of using truthiness
x = 2
if x == True:
    print("won't print")       # 2 == True is False

# Correct:
if x:
    print("prints")            # prints because 2 is truthy

# (3) Checking emptiness with == [] instead of truthiness
lst = []
if lst == []:
    print("empty list")        # works but unnecessary and narrow

# Better:
if not lst:
    print("empty (idiomatic)") # works for any empty container


# ============================================================
# 8) Summary (one-screen mental rules)
# ============================================================

# if x:         -> checks truthiness (not x == True)
# falsy values  -> False, None, 0, 0.0, "", empty containers
# and/or        -> return operands:
# From a short-circuit perspective, and and or return the value where evaluation stopped.
#                 a and b -> first falsy, else last
#                 a or b  -> first truthy, else last
# short-circuit -> second operand may not be evaluated


# ============================================================
# 9) Quick self-check examples (expected outputs in comments)
# ============================================================
#From a short-circuit perspective, and and or return the value where evaluation stopped.
print([0] and "X")          # "X"   ([0] is truthy, return last)
print([] and "X")           # []    ([] is falsy, return first falsy)
print([] or "X")            # "X"   ([] is falsy, return first truthy)
print("Y" or "X")           # "Y"   ("Y" is truthy, return it)

x = [0]
if x:
    print("A")              # A (non-empty list is truthy)
else:
    print("B")
