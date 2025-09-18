

def countdown():
    print("Countdown startet!")
    yield 3
    print("Nach der 3")
    yield 2
    print("Nach der 2")
    yield 1
    print("Nach der 1")
    yield "Start!"
    print("Countdown fertig!")

for schritt in countdown():
    print(f"-> {schritt}")

#################################################################################
print("-"*50)
def count_up_to(n):
    i = 1
    while i <= n:
        yield i  # erzeugt einen Wert und pausiert die Funktion
        i += 1

counter = count_up_to(5)

print(next(counter)) # 1
print(next(counter)) # 2
print("-")
for number in counter:
    print(number)

