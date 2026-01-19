# ============================================================
# Topic 04 — Dictionaries
# ============================================================

# A dictionary is a MUTABLE mapping: key -> value
# Mutation changes the object IN PLACE.

d = {"name": "Ray", "age": 20}

# ---- Access ----
print(d["name"])          # "Ray"

# ---- Mutation (add / overwrite) ----
d["age"] = 21             # overwrite existing key
d["city"] = "Omaha"       # add new key
print(d)                  # {'name': 'Ray', 'age': 21, 'city': 'Omaha'}

# ---- Safe access with get() ----
print(d.get("age"))       # 21
print(d.get("missing"))   # None
print(d.get("missing", 0))# 0

# ---- Keys, values, items ----
print(d.keys())           # dict_keys(['name', 'age', 'city'])
print(d.values())         # dict_values(['Ray', 21, 'Omaha'])
print(d.items())          # dict_items([('name','Ray'), ('age',21), ('city','Omaha')])

# ---- pop (remove + return) ----
age = d.pop("age")
print(age)                # 21
print(d)                  # {'name': 'Ray', 'city': 'Omaha'}

# ---- update (bulk insert) ----
d.update({"job": "student", "year": 3})
print(d)                  # {'name':'Ray','city':'Omaha','job':'student','year':3}

# ---- clear (empties dict) ----
tmp = {"x": 1}
tmp.clear()
print(tmp)                # {}

# ---- Mutation vs rebinding ----
a = {"x": 1}
b = a
a["y"] = 2                # mutation
print(a)                  # {'x': 1, 'y': 2}
print(b)                  # {'x': 1, 'y': 2}

a = {"z": 9}              # rebinding
print(a)                  # {'z': 9}
print(b)                  # {'x': 1, 'y': 2}

# ---- Key rules ----
# Keys must be IMMUTABLE and hashable.
# Values can be anything.

good = {(1, 2): "point"}  # OK: tuple is immutable
# bad = {[1, 2]: "x"}     # ❌ error: list is mutable
