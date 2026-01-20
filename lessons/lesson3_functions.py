# ----- Core mental model: names vs objects -----
# A Python "variable" is a NAME, not a box holding the value.
# The name points to an OBJECT in memory.
# Rebinding changes what a name points to.
# Mutation changes the object itself (so all names pointing to it see the change).





# ----- Functions: parameters become new names -----
# When you call a function, Python does NOT pass the original"variable" (name).
# the function parameter becomes a completely new name that points to the same object of the caller.
# Two names. One object.

def rebind_list(lst):
    # lst is a NEW name inside the function that points to same object as nums.
    lst = [9, 9]  # rebinding: lst now points to a NEW list object; caller (nums) not affected

nums = [1, 2]
rebind_list(nums)
print(nums)      # [1, 2] because only lst changed, not the original list object






# ----- Mutation vs rebinding inside functions -----
def f(x):
    # x is a NEW name bound to the SAME object as the caller's list
    # Two names. One object.
    x.append(99)  # MUTATION: changes the existing list object in place

def g(x):
    # x is a NEW name bound to the SAME object as the caller's list (at start)
    # But this line creates a NEW list and REBINDS x to it
    x = x + [99]  # REBINDING: caller's list object is not changed

a = [1, 2]
f(a)             # caller passes reference to the list; x points to same list; mutation happens
print(a)         # [1, 2, 99]

b = [1, 2]
g(b)             # x is rebound inside function; b still points to original list
print(b)         # [1, 2]





# ----- Proving "Two names. One object." with id() -----
# id() returns an identity number for the object (in CPython it often matches the memory address).
# Treat it as an ID you can compare, not something you manipulate.

lst1 = [1, 2]
lst2 = lst1
print(id(lst1), id(lst2))   # same ID → same object

lst1.append(3)              # mutation does not change the object identity
print(id(lst1), id(lst2))   # still same ID

lst1 = lst1 + [4]           # rebinding creates a new list object
print(id(lst1), id(lst2))   # now different IDs
print(lst1, lst2)           # [1, 2, 3, 4] and [1, 2, 3]
