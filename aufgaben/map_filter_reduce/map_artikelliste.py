

artikel = [
    {"name": "32 Gb RAM", "price": 99.87},
    {"name": "1 TB SSD", "price": 234.99},
    {"name": "Maus", "price": 19.99},
]


# den bruttopreis berechnen - 19% aufschlagen
# und als neues feld anfügen

artikel_brutto = list(map(lambda artikel: {**artikel, "brutto": artikel["price"] * 1.19}, artikel))
print(artikel_brutto)


