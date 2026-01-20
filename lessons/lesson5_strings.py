# ============================================================
# Topic 01 — Strings
# ============================================================

# A string is an IMMUTABLE sequence of characters.
# Immutable means the object cannot be changed in place.

s = "hello"

# Indexing is allowed (read-only)
print(s[0])      # 'h'
print(len(s))    # 5

# This is NOT allowed (no mutation)
# s[0] = "H"     # error

# "Changing" a string creates a NEW object
s = s + "!"
print(s)         # "hello!"

# String methods return NEW strings
t = s.upper()
print(s)         # "hello!"
print(t)         # "HELLO"

# Key rule:
# Strings behave like read-only lists (similar to tuples)
