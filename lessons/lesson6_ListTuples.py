# ============================================================
# Topic 02 — Lists (mutable sequence)
# ============================================================

# Mental model:
# - A list is a MUTABLE object (its contents can change IN PLACE).
# - Variables are names pointing to objects.
# - If two names point to the same list, mutation affects both.

lst = [10, 20, 30]

# ---- Indexing (read) ----
print(lst[0])      # 10
print(lst[-1])     # 30 (last element)
print(len(lst))    # 3

# ---- Mutation: append (adds to end) ----
lst.append(40)     # mutates in place
print(lst)         # [10, 20, 30, 40]

# ---- Mutation: extend (adds many to end) ----
lst.extend([50, 60])
print(lst)         # [10, 20, 30, 40, 50, 60]

# ---- Mutation: insert (adds at an index) ----
lst.insert(1, 15)  # insert 15 at index 1
print(lst)         # [10, 15, 20, 30, 40, 50, 60]

# ---- Mutation: pop (removes and returns) ----
# pop() removes from the END by default
last = lst.pop()
print(last)        # 60
print(lst)         # [10, 15, 20, 30, 40, 50]

# pop(i) removes index i
first = lst.pop(0)
print(first)       # 10
print(lst)         # [15, 20, 30, 40, 50]

# ---- Mutation: remove (removes by VALUE, first match) ----
lst.remove(30)
print(lst)         # [15, 20, 40, 50]

# ---- Mutation: clear (removes everything) ----
tmp = [1, 2, 3]
tmp.clear()
print(tmp)         # []

# ---- Membership test ----
print(20 in lst)   # True
print(99 in lst)   # False

# ---- Slicing (creates a NEW list, does NOT mutate) ----
# slice is "copy out a range"
sub = lst[1:3]
print(sub)         # e.g. [20, 40]
print(lst)         # original unchanged

# ---- Sorting ----
# sorted(lst) returns a NEW list (does not mutate lst)
sorted_copy = sorted(lst)
print(sorted_copy)
print(lst)

# lst.sort() mutates the list in place
lst.sort()
print(lst)

# ---- Rebinding vs mutation ----
a = [1, 2]
b = a              # b points to the same list object as a
a.append(3)        # mutation affects both
print(a)           # [1, 2, 3]
print(b)           # [1, 2, 3]

a = [9, 9]         # rebinding: a now points to a new list object
print(a)           # [9, 9]
print(b)           # [1, 2, 3]


# ============================================================
# Topic 03 — Tuples (immutable sequence)
# ============================================================

# Mental model:
# - A tuple is like a read-only list.
# - You can read/index/iterate, but you cannot change it in place.

t = (10, 20, 30)

# ---- Indexing and length ----
print(t[0])        # 10
print(t[-1])       # 30
print(len(t))      # 3

# ---- Tuples are immutable (no mutation allowed) ----
# t.append(40)     # ❌ error: tuple has no append
# t[0] = 99        # ❌ error: cannot assign to tuple item

# ---- Tuple packing (no parentheses required) ----
p = 1, 2, 3
print(p)           # (1, 2, 3)

# ---- Unpacking ----
x, y, z = p
print(x, y, z)     # 1 2 3

# ---- Common tuple methods (very few) ----
t2 = (1, 2, 2, 3)
print(t2.count(2)) # 2  (how many times 2 appears)
print(t2.index(3)) # 3  (first index where value 3 appears)

# ---- Why tuples are used ----
# Use tuples for fixed data that should not change:
# - coordinates (x, y)
# - RGB colors (r, g, b)
# - returning multiple values from a function

coords = (5, 8)
rgb = (255, 0, 0)
print(coords, rgb)

# ---- Important detail ----
# A tuple is immutable, but it can CONTAIN mutable objects.
# The tuple itself cannot change which objects it points to,
# but a mutable object inside it can still be mutated.

inside = ([1, 2], [3, 4])
inside[0].append(99)          # mutates the inner list (allowed)
print(inside)                 # ([1, 2, 99], [3, 4])
