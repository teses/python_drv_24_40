"""
# Erkennung eines deutschen KFZ Kennzeichens

3 2 4
"""
import re

kennzeichen = [
    "WÜ AB 12", # True
    "B AB 1", # True
    "B M 1", # True
    "WES BU 1234", # True
    "WES A 1234", # True
    "WES A 12345", # False
    "WES A 1000E", # True
    "WÜ AB 12E", # True
    "B AB 1E", # True
    "B M 1E", # True
    "DU ME 123", # True
    "DU ME 123H", # True
    "DU ME 123E", # True
    " DU ME 123H ",  # False
    " ABC A 123", # False
    "WEST 123", # False
    "WEST A 1", # False
    "N ABC 11", # False
    "N ABC", # False
    "N 11", # False
]

muster       = r"(^[^\s]{1,3})\s([^\s]{1,2})\s[0-9]{1,4}[HE]?$"
musterThomas = r"^[A-Z]{1,3}\s[A-Z]{1,2}\s[0-9EH]+$"


for k in kennzeichen:
    res = re.search(muster , k)
    print(k, "True" if res else "False")
