

mitarbeiter = [
    {"name": "Anna", "abteilung": "IT", "jahr": 2020},
    {"name": "Bernd", "abteilung": "HR", "jahr": 2019},
    {"name": "Clara", "abteilung": "IT", "jahr": 2020},
    {"name": "Dieter", "abteilung": "Marketing", "jahr": 2021},
    {"name": "Eva", "abteilung": "HR", "jahr": 2019}
]

# Diese Funktion wird auf jedes Element in der Liste angewendet
def meine_sortierung(person):
    return person["abteilung"]

# sortiert mit callback
mitarbeiter.sort(key=meine_sortierung)

# sortiert mit lambda nach jahr

for m in mitarbeiter:
    print(m)
