




def counter():
    count = 0

    def incr():
        nonlocal count
        count += 1
        return count

    return incr



def counter2():
    count = [0]

    def incr():
        count[0] += 1 # ohne nonlocal muss es ein veränderbarer Datentyp sein (mutable)
        return count[0]

    return incr



z1 = counter2()
z2 = counter2()

print("z1", z1())
print("z1", z1())
print("z1", z1())

print("z2", z2())
print("z2", z2())

print("z1", z1())