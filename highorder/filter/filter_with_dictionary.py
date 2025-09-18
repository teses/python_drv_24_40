

personen = [
    {"name": "Max", "alter": 25},
    {"name": "Bob", "alter": 18},
    {"name": "Clara", "alter": 30},
    {"name": "David", "alter": 15},
    {"name": "Emma", "alter": 15},
]

# alle älter als 18
result = list(filter(lambda p : p["alter"]>= 18, personen))
print(result)

# alle Frauen # personen die mit a enden
frauen = list(filter(lambda p: p["name"].endswith("a"), personen))
print(frauen)

#
frauen = list(filter(lambda p: p["alter"]>= 18 and p["name"].endswith("a"), personen))
print(frauen)
