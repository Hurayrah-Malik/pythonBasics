"""
Python Study Notes — *args, **kwargs, and * / ** Unpacking

GOAL:
Understand exactly how Python binds arguments to parameters.
No guessing. No "magic".

------------------------------------------------------------
MENTAL MODEL (MEMORIZE)
------------------------------------------------------------
When calling a function, Python assigns arguments in this order:

1) Positional arguments fill named parameters left-to-right.
2) Remaining positional arguments are PACKED into *args (a tuple).
3) Keyword arguments match named parameters by name.
4) Remaining keyword arguments are PACKED into **kwargs (a dict).

IMPORTANT:
- `args` and `kwargs` are just conventional NAMES.
  You can rename them, but you MUST keep the * and ** syntax markers.
- `*` and `**` are SYNTAX, not variable names.
  You cannot write:  * = 5   (invalid)
"""

# ============================================================
# 1) Basic *args and **kwargs collection
# ============================================================


def test(x, y, *args, **kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)


test(1, 2, 5, 6, a=3, b=4)

# Output:
# 1
# 2
# (5, 6)
# {'a': 3, 'b': 4}

# Why:
# - x gets the first positional argument: 1
# - y gets the second positional argument: 2
# - extra positional args (5, 6) are packed into args as a tuple
# - keyword args (a=3, b=4) are packed into kwargs as a dict


# ============================================================
# 2) Mixing positional + keyword (valid when each param is assigned once)
# ============================================================

test(1, y=2, a=3)

# Output:
# 1
# 2
# ()
# {'a': 3}

# Why:
# - x is filled positionally: x=1
# - y is filled by keyword: y=2
# - no extra positional args -> args=()
# - 'a' is not a named param, so it goes into kwargs


# Keyword order does not matter:
test(y=1, x=2)

# Output:
# 2
# 1
# ()
# {}

# Why:
# - keyword arguments match parameters BY NAME, not by position/order


# ============================================================
# 3) Common INVALID calls (your confusions)
# ============================================================

# Confusion A: "test(x=1, 2) should bind y=2"
# WRONG: this is invalid syntax.
#
# Rule:
# - positional arguments MUST come BEFORE keyword arguments.

# test(x=1, 2)
# SyntaxError: positional argument follows keyword argument


# Confusion B: "test(y=1, x=2, x=3) puts x=3 into kwargs"
# WRONG: duplicates do NOT go into kwargs.
#
# Rule:
# - you cannot assign the same parameter twice.

# test(y=1, x=2, x=3)
# TypeError: test() got multiple values for argument 'x'


# Another duplicate example (also invalid):
# test(1, a=2)  # a is a parameter name in this function? No, but this one depends on function signature.
# For our test(x, y, *args, **kwargs), this is valid because 'a' is not x or y.
# But for a function like f(a, b, *args, **kwargs), passing a twice can happen.


def f(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


# f(1, a=2)
# TypeError: f() got multiple values for argument 'a'
#
# Why:
# - positional 1 assigns a=1
# - keyword a=2 tries to assign a again


# ============================================================
# 4) What * means in a parameter list
# ============================================================

# There are TWO related uses of * in function definitions:


# (1) *args: pack extra positional arguments into a tuple called args
def pack_positional(*args):
    print(args)


pack_positional(1, 2, 3)
# Output:
# (1, 2, 3)


# (2) bare * (no name): everything AFTER must be keyword-only
def g(a, *, b):
    print(a, b)


# g(1, 2)
# TypeError: g() takes 1 positional argument but 2 were given
#
# Why:
# - after the bare *, b MUST be passed by keyword

g(1, b=2)
# Output:
# 1 2


# ============================================================
# 5) What * means at the CALL site: unpacking positional arguments
# ============================================================

vals = [10, 20, 30]
f(*vals)

# Output:
# 10
# 20
# (30,)
# {}

# Why:
# - f(*vals) is equivalent to f(10, 20, 30)
# - a=10, b=20
# - extra positional 30 goes into args
#
# IMPORTANT TUPLE SYNTAX:
# - args prints (30,) not (30)
# - (30) is just 30 in parentheses
# - (30,) is a one-element tuple


# ============================================================
# 6) What ** means at the CALL site: unpacking keyword arguments from a dict
# ============================================================

data = {"a": 5, "b": 6}
f(**data)

# Output:
# 5
# 6
# ()
# {}

# Why:
# - f(**data) is equivalent to f(a=5, b=6)
# - kwargs is empty because all keywords matched named parameters


# ============================================================
# 7) Mixed unpacking (* and **) together
# ============================================================

f(1, 2, *[3, 4], **{"x": 5})

# Output:
# 1
# 2
# (3, 4)
# {'x': 5}

# Why:
# - *[3, 4] expands into extra positional arguments: 3, 4
# - **{'x': 5} expands into keyword argument: x=5
# - x is not a named parameter of f(a, b, ...), so it goes into kwargs


# ============================================================
# 8) More tricky examples (with answers)
# ============================================================

# Q1
f(1, b=2, c=3)
# Output:
# 1
# 2
# ()
# {'c': 3}
#
# Why:
# - a=1 positionally
# - b=2 by keyword (matches parameter)
# - c=3 doesn't match a or b, so goes into kwargs

# Q2
f(1, 2, 3, 4)
# Output:
# 1
# 2
# (3, 4)
# {}
#
# Why:
# - extra positional args go into *args

# Q3 (duplicate assignment)
# f(1, **{'b': 2}, a=9)
# TypeError: f() got multiple values for argument 'a'
#
# Why:
# - positional 1 assigns a=1
# - then a=9 tries to assign a again

# Q4 (keyword from dict + explicit keyword duplicates)
d = {"b": 2}
# f(1, **d, b=3)
# TypeError: f() got multiple values for keyword argument 'b'
#
# Why:
# - **d provides b=2
# - b=3 tries to assign b again


# ============================================================
# 9) Keyword-only after *args (related to the bare * idea)
# ============================================================


def h(*args, b):
    print(args, b)


h(1, 2, b=3)
# Output:
# (1, 2) 3
#
# Why:
# - *args collects positional arguments
# - parameters after *args (like b) are keyword-only automatically


# ============================================================
# 10) Exercises (solve WITHOUT running first, then verify)
# ============================================================

# Exercise 1: predict output
# f(1, **{'b': 2, 'c': 3})
#
# Exercise 2: predict whether this is valid, and why
# f(a=1, 2)
#
# Exercise 3: predict output or error, and the rule violated
# f(1, a=2)

"""
EXPECTED ANSWERS (don't read until after you try):

Exercise 1:
- a=1
- b=2
- args=()
- kwargs={'c':3}

Exercise 2:
- SyntaxError: positional argument follows keyword argument

Exercise 3:
- TypeError: f() got multiple values for argument 'a'
"""
