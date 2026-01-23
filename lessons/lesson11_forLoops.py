"""
Python Study Notes — Iteration Basics (for-loops), Indexing Helpers (len/range/enumerate),
and Scope Footguns

You are building mental models, not memorizing syntax.

CORE MENTAL MODELS
1) `for` loops:
   - A `for` loop repeatedly rebinds ONE name to successive elements.
   - The loop variable is just a NAME (a reference), not a “slot in the list”.
   - Rebinding the loop variable does NOT change the container.

2) Mutability:
   - If the element is mutable (like a list), mutating it (e.g., .append) changes the original object.
   - If you rebind a name (x = ...), you do NOT change the original object—only what the name points to.

3) No new scope:
   - Python `for` loops do NOT create a new scope.
   - Names created inside the loop remain after the loop ends (in the same surrounding scope).

4) Helpers you must understand:
   - len(container) -> number of elements
   - range(n) -> 0..n-1 (produces valid indexes)
   - enumerate(iterable) -> (index, element) pairs, produced lazily

Industry standards to avoid bugs:
- Use descriptive loop variable names (avoid reusing important names)
- Put larger logic in functions to keep variable lifetimes tight
- Use a linter (e.g., Ruff) to warn about name reuse/shadowing
"""

# ============================================================
# 1) len(): count elements (NOT indexes)
# ============================================================

nums = [10, 20, 30]
print(len(nums))  # 3

# Indexes are always 0 .. len(nums)-1
# For [10, 20, 30], valid indexes are 0, 1, 2


# ============================================================
# 2) range(): produces a sequence of integers
# ============================================================

print(list(range(5)))  # [0, 1, 2, 3, 4]

for i in range(3):
    print(i)
# Output:
# 0
# 1
# 2

# range(n) yields numbers from 0 up to (but not including) n


# ============================================================
# 3) Critical rule: the loop variable is just a name
# ============================================================

nums = [1, 2, 3]

for x in nums:
    x = 100

print(nums)
# Output:
# [1, 2, 3]
#
# Why:
# - x is rebound to 100
# - This does not affect the list
# - You changed the name `x`, not the objects inside `nums`

# ------------------------------------------------------------
# Correct way to change numbers inside a list during a loop:
# modify the list itself using indexes
# ------------------------------------------------------------

nums = [1, 2, 3]

for i in range(len(nums)):
    nums[i] = nums[i] * 10

print(nums)
# Output:
# [10, 20, 30]
#
# Why:
# - i iterates over valid indexes (0..len(nums)-1)
# - nums[i] targets the element slot in the list
# - you replace the element in the list, not just rebind a loop name


# ============================================================
# 4) Rebinding vs mutation with nested lists
# ============================================================

nums = [[1], [2], [3]]

for x in nums:
    x = [0]

print(nums)
# Output:
# [[1], [2], [3]]
#
# Why:
# - x is just a name
# - x = [0] rebinds x to a new list object
# - the original inner lists in nums are untouched

# ------------------------------------------------------------
# Correct way to replace each inner list with [0]:
# ------------------------------------------------------------

nums = [[1], [2], [3]]

for i in range(len(nums)):
    nums[i] = [0]

print(nums)
# Output:
# [[0], [0], [0]]
#
# Why:
# - nums[i] accesses the container storage
# - you replace each element of nums with a new list [0]


# ============================================================
# 5) Another critical rule: `for` does NOT track indexes
# ============================================================

for x in [10, 20, 30]:
    print(x)

# There is:
# - No counter
# - No index
# - No “position” unless you add one


# ============================================================
# 6) enumerate(): index + element pairs (lazy)
# ============================================================

values = ["a", "b", "c"]

# enumerate without a for-loop:
e = enumerate(values)
print(e)
# Output (typical):
# <enumerate object at 0x...>
#
# Why:
# - enumerate(values) creates an iterator object
# - it produces pairs only when iterated/consumed

print(list(enumerate(values)))
# Output:
# [(0, 'a'), (1, 'b'), (2, 'c')]

# enumerate in a loop (printing the pairs):
for pair in enumerate([10, 20, 30]):
    print(pair)
# Output:
# (0, 10)
# (1, 20)
# (2, 30)

# Unpacking the pairs into two names:
for i, x in enumerate([10, 20, 30]):
    print(i, x)
# Output:
# 0 10
# 1 20
# 2 30
#
# Why:
# - enumerate produces (index, element)
# - i gets the index, x gets the element


# ============================================================
# 7) for-loops do NOT create a new scope (names persist)
# ============================================================

for x in [1, 2, 3]:
    pass

print(x)
# Output:
# 3
#
# Why the output is 3 (step-by-step):
# - Iteration 1: x is bound to 1
# - Iteration 2: x is rebound to 2
# - Iteration 3: x is rebound to 3
# - Loop ends, Python does NOT delete x
# - x remains bound to the last value: 3

# Variables created inside the loop body also remain:
for i in [1, 2, 3]:
    y = i * 10

print(y)
# Output:
# 30
#
# Why:
# - y is created in the surrounding scope
# - the loop does not create a new scope
# - y remains bound after the loop to its last value (30)


# ============================================================
# 8) Common footgun: accidentally overwriting an important name
# ============================================================

x = "important value"

for x in [1, 2, 3]:
    pass

print(x)
# Output:
# 3
#
# Why:
# - you reused the name `x`
# - the loop rebinds x repeatedly
# - after the loop, x remains bound to the last value (3)
# - the original "important value" is lost (overwritten)

# ------------------------------------------------------------
# Industry standard prevention: use descriptive loop variables
# ------------------------------------------------------------

value = "important value"

for num in [1, 2, 3]:
    pass

print(value)
# Output:
# important value


# ============================================================
# 9) Industry standard prevention: use functions to limit name lifetime
# ============================================================

def demo_scope():
    x = "important value"
    for x in [1, 2, 3]:
        pass
    print("inside function x:", x)

demo_scope()
print("outside function: the x inside demo_scope does not leak here")
# Note:
# - Inside the function, x ends as 3
# - Outside, that x is not in scope (it was local to the function)
