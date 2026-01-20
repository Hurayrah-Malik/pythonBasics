# ============================================================
# SETS STUDY FILE — Mental models + examples
# ============================================================

# ----- What a set is (plain terms) -----
# A set is a collection for FAST membership testing:
#    "Is x in here?"
#
# A set does NOT:
# - keep meaningful order
# - support indexing like s[0]
# - allow duplicates
#
# A set DOES:
# - store unique elements
# - make "x in s" fast on average (usually O(1))


# ----- Important distinction: set mutability -----
# The *set object itself* is MUTABLE:
#   you can add/remove elements.
#
# The *elements inside* must be HASHABLE (immutable) :
#   their hash value must NOT change while stored in the set. if an objects value changes in the hashmap
#   its hash should change (but doesn't) then it's "lost" in the set.
#
# "Hashable" usually means: immutable value (int, str, tuple-of-immutables, etc.)

s = set()
s.add(10)
s.add(20)
print(s)  # example output: {10, 20}  (order not guaranteed)

#the set objects are stored in an array of "buckets" internally for fast lookup. 
# each bucket can hold multiple objects in case of hash collisions.
# ----- Hash: what it is and what it isn't -----
# hash(x) produces an integer derived from x's value.
# It is NOT:
# - a memory address
# - a bucket index directly
#
# Instead:
#   hash(x) ---> (math using table size) ---> bucket index
#
# Two different sets can both contain 10.
# The hash of 10 is the same integer in both sets (for ints),
# but each set has its OWN internal table and buckets.

a = {10}
b = {10}

print(hash(10), hash(10))  # same number printed twice
print(10 in a, 10 in b)    # True True


# ----- How lookup works (mental model) -----
# When you do:  x in s
# Python does roughly:
# 1) compute h = hash(x)
# 2) convert h into a bucket index i (depends on the set's table size)
# 3) check bucket i:
#    - if empty: x not present
#    - if occupied: compare using == to confirm match or handle collision
#
# Collisions: two different values can land in the same bucket.
# Then Python uses == to decide if it's really the same value or a different one.


# ----- Why lists cannot be in sets -----
# Lists are mutable, so their "value" can change.
# If a list were allowed in a set, changing it could change its hash,
# which would "misplace" it in the table.
#
# Python prevents this by making lists unhashable.

try:
    bad = {[1, 2, 3]}
except TypeError as e:
    print("Lists can't be in sets:", e)


# ----- Why tuples CAN be in sets (sometimes) -----
# Tuples are immutable, so they are usually hashable.
# BUT: a tuple is only hashable if ALL its contents are hashable.

ok = {(1, 2), (3, 4)}
print(ok)  # set of tuples is fine

try:
    bad_tuple = {(1, [2, 3])}  # contains a list inside the tuple
except TypeError as e:
    print("Tuple containing list can't be in sets:", e)


# ----- True == 1 (and why sets treat them as duplicates) -----
# In Python, bool is a subclass of int.
# That means True behaves like 1 and False behaves like 0 in comparisons and hashing.

print(True == 1)           # True
print(False == 0)          # True
print(hash(True) == hash(1))   # True (required by hash-table correctness)

x = {True, 1}
print(x)  # only one element, because True and 1 compare equal and share hash


# ----- Order: do NOT rely on it -----
# Set iteration order is not meant to be stable for your program logic.
# It can change based on internal resizing and hashing behavior.

demo = {10, 20, 30, 40, 50}
for item in demo:
    print("iter:", item)
# output order may vary


# ----- Cross-run hash stability: ints vs strings -----
# Integers: stable hashing.
print("hash(10):", hash(10))

# Strings: Python intentionally randomizes hashing per process for security.
# That means hash("hello") may differ between different runs of Python.
print('hash("hello"):', hash("hello"))


# ----- Collision demonstration (conceptual) -----
# It is hard to "force" a collision reliably without digging into implementation,
# because Python's hashing is designed well.
# The key takeaway:
# - collisions can happen
# - correctness is preserved by checking equality (==) after hashing


# ============================================================
# Mini-tool: Duplicate detector (practice)
# ============================================================
# Goal: use a set as a fast "seen" tracker.

data = [1, 2, 3, 2, 1,1, 1, True, 4]

seen = set()
dupes = []

for value in data:
    if value in seen:
        dupes.append(value)
    else:
        seen.add(value)

print("data:", data)
print("seen:", seen)
print("dupes:", dupes)

# Notice something important:
# - True is treated as duplicate of 1 (because True == 1)
# So depending on the order of the list, you may see True flagged as duplicate
# or 1 flagged as duplicate.
