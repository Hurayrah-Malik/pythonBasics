"""
Comparison, Identity, and Truthiness (Python) — Study Notes

Core ideas:
- Objects have identity (which object it is) and value (what it represents)
- Python provides different tools for different questions

Key rules (memorize):
- `is`     -> identity comparison (same object)
- `==`     -> value comparison (same contents)
- `if x:`  -> truthiness check (NOT equality to True)

CRITICAL:
- Use `is` ONLY for identity (especially None)
- Use `==` for values
- Use truthiness for control flow
"""

# ============================================================
# 1) Identity vs Equality
# ============================================================

a = [1, 2]
b = a
c = [1, 2]

print(a == b)    # True  (same contents)
print(a is b)    # True  (same object)

print(a == c)    # True  (same contents)
print(a is c)    # False (different objects)

# Key idea:
# - Equality does NOT imply identity
# - Identity almost always implies equality


# ============================================================
# 2) None: identity check ONLY
# ============================================================

x = None

# CORRECT
if x is None:
    print("x is None")

# WRONG (do not do this)
# if x == None:
#     pass

# Why:
# - `==` calls __eq__ and can be overridden
# - `None` is a singleton (only one None object exists)
# - Identity is the only safe check


# ============================================================
# 3) Truthiness vs True / False
# ============================================================

x = 1

# CORRECT: truthiness check
if x:
    print("x is truthy")

# WRONG: equality to True
if x == True:
    print("x == True")   # does NOT print (1 == True is True, but don't rely on this)

# WRONG: identity with True
if x is True:
    print("x is True")   # does NOT print (x is an int, not the True object)

# Key idea:
# - `if x:` asks "is x truthy?"
# - `== True` asks "does x equal True?"
# - `is True` asks "is x the True object?"


# ============================================================
# 4) True and False are singletons (but still not for control flow)
# ============================================================

print(True is True)      # True
print(False is False)    # True

x = True

print(x is True)         # True
print(x == True)         # True
print(bool(x))           # True

# Even though this works, DO NOT write:
# if x is True:
# Use:
# if x:


# ============================================================
# 5) Numbers: value comparison ONLY
# ============================================================

x = 0

# CORRECT
if x == 0:
    print("x is zero")

# WRONG
# if x is 0:
#     pass

# Why:
# - 0 is a value, not a sentinel
# - identity for numbers is an implementation detail
# - using `is` here is asking the wrong question


# ============================================================
# 6) Chained comparisons
# ============================================================

x = 5

if 1 < x < 10:
    print("x is between 1 and 10")

# This is equivalent to:
# (1 < x) and (x < 10)
# but `x` is evaluated only once

# This avoids bugs if x is:
# - a function call that would change value of x
# - a property
# - an expression with side effects


# ============================================================
# Summary (commit this)
# ============================================================

# - Use `is` only for identity (None, sentinels)
# - Use `==` for value comparison
# - Use truthiness (`if x:`) for control flow
# - Never rely on `is` for numbers or strings
# - Never use `is True` or `is False` in normal code
