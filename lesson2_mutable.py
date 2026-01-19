# integers are immutable. immutable means once the object is created, its content cannot be changed. any change creates a new object in memory.
# immutable objects include: int, float, str, tuple, bytes, frozenset, range, bool
a = 10                      # a now points to an int object with value 10
b = a                       # b points to the same int object as a (no copy is made)
a = a + 1                   # a + 1 creates a new int object (11); a is rebound to it
print(a)                    # 11
print(b)                    # 10


# lists are mutable. mutable means the content of the object can be changed without creating a new object in memory.
# mutable objects include: list, dict, set, bytearray, most custom objects
x = [1, 2]
y = x                       # x and y point to the same list object
x.append(3)                 # mutation: modifies the existing list object
print(x)                    # [1, 2, 3]
print(y)                    # [1, 2, 3]


# rebinding means pointing a variable to a new object in memory
a = [1, 2]
b = a                       # b points to the same list object as a
a = [9, 9]                  # rebinding a; does not affect b
print(a)                    # [9, 9]
print(b)                    # [1, 2]


# dictionary example of mutation
config = {"mode": "dev"}
alias = config              # alias points to the same dictionary object
config["mode"] = "prod"     # mutation: changes the shared object
print(config)               # {'mode': 'prod'}
print(alias)                # {'mode': 'prod'}


# dictionary example of rebinding
config = {"mode": "dev"}
alias = config
config = {"mode": "prod"}   # rebinding config to a new dictionary
print(config)               # {'mode': 'prod'}
print(alias)                # {'mode': 'dev'}


# rebinding example (NO mutation)
a = [10, 20]
b = a
a = a + [30]                # creates a new list; a is rebound
print(a)                    # [10, 20, 30]
print(b)                    # [10, 20]


# mutation example (shared object is changed)
c = [10, 20]
d = c
c.append(30)                # mutates the existing list
print(c)                    # [10, 20, 30]
print(d)                    # [10, 20, 30]



# using id() to show same object vs new object in memory
x = [1, 2]
y = x
print(id(x), id(y))         # same id → same object
x.append(3)                 # mutation
print(id(x), id(y))         # still same id
x = x + [4]                 # rebinding (new object)
print(id(x), id(y))         # different ids


# function example: mutation affects the caller
def add_item(lst, item):
    lst.append(item)        # mutates the list passed in

nums = [1, 2]
add_item(nums, 3)
print(nums)                 # [1, 2, 3]
