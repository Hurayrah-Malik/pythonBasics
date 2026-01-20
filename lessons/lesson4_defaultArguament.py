# ============================================================
# LESSON 4 — Default Arguments, Scope, and Lifetime
# ============================================================

# ------------------------------------------------------------
# Core ideas
# ------------------------------------------------------------
# 1. Variables in Python are NAMES that point to OBJECTS.
# 2. Function parameters are LOCAL names.
# 3. Local names exist only while the function is executing.
# 4. Objects live as long as something references them.
# 5. Default arguments (defining something in the function parameters) are evaluated ONCE, when the function is defined,
#    NOT every time the function is called.

# ------------------------------------------------------------
# Default argument trap — what NOT to do
# ------------------------------------------------------------
# Because `lst = []` in a function parameter list is NOT an assignment that runs on every call.
#
# It runs ONCE, when Python DEFINES the function.
#
# def add_item(item, lst=[]):
# This line:
# - runs once
# - when Python defines the function
# - NOT every time the function is called
#
# As a result, the SAME list object is reused across calls.


# BAD: mutable default argument (shared across calls)
# remember: default arguments are evaluated ONCE, when the function is defined, and lists are mutable,
# therefore it keeps growing
def bad_add(item, lst=[]):
    lst.append(item)
    return lst

print(bad_add(1))  # [1]
print(bad_add(2))  # [1, 2]
print(bad_add(3))  # [1, 2, 3]


# ------------------------------------------------------------
# Example that DOES rebind every call
# ------------------------------------------------------------
# This works because the list is created INSIDE the function body,
# and code inside the function runs EVERY time the function is called.

def f():
    x = []          # runs every call, therefore a NEW list is created each time
    x.append(1)
    return x        #x is destroyed after function exits

print(f())  # [1]
print(f())  # [1]


# ------------------------------------------------------------
# Correct pattern — safe default arguments
# ------------------------------------------------------------
# Use None as the default and create any mutable object INSIDE the function (like a list).

def good_add(item, lst=None):
    # lst starts as None on EACH call if the caller does not provide it
    if lst is None:
        lst = []    # NEW list created every call

    # This list exists ONLY for this call
    # It is NOT stored as a default
    # It is NOT reused later because the lst variable will be destroyed when the function exits

    lst.append(item)
    return lst

print(good_add(1))  # [1]
print(good_add(2))  # [2]
print(good_add(3))  # [3]


# ------------------------------------------------------------
# What happens when a function exits
# ------------------------------------------------------------
# - Local variable names (like lst or x) are destroyed
# - Objects are destroyed ONLY if no references remain

def example():
    x = "hello"     # x is a local name
    return x

y = example()
# x no longer exists, but "hello" still exists because y refers to it


# ------------------------------------------------------------
# Important clarification about default arguments
# ------------------------------------------------------------
#
# Using lst=[] in the function parameters does NOT create a normal local variable.
# That list is created ONCE, before the function is ever called, and stored inside
# the function object itself.
#
# Because it is mutable and reused across calls, it keeps accumulating changes.
# This makes it behave like shared state attached to the function (similar to a global),
# even though it is not accessible outside the function by name.
#
# Using lst=None avoids this problem because:
# - None is immutable
# - The list is created INSIDE the function body
# - Code inside the function runs every call
#
# In the lst=None pattern:
# - lst is a local name
# - it can point to any object during the call
# - when the function exits, the name lst is destroyed
# - the next call starts fresh with lst = None again


# ------------------------------------------------------------
# General rule (memorize this)
# ------------------------------------------------------------
# Never use mutable objects as default function arguments.
# This applies to:
# - lists
# - dicts
# - sets
# - custom mutable objects

