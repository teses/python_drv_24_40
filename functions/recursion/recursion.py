"""

    Was ist Rekursion?

    Rekursion bedeutet, dass eine Funktion sich selbst aufruft, um ein Problem zu lösen.

    Jede rekursive Funktion braucht mindestens zwei Dinge:

    - Basisfall – das ist die Bedingung, bei der die Rekursion endet.
    - Rekursiver Fall – hier ruft sich die Funktion selbst auf, aber mit einem kleineren/simpleren Problem.

"""

import time

def countdown(n):
    # Basisfall
    if n == 0:
        print("fertig")

    else:
        print(n)
        time.sleep(1)
        countdown(n - 1)

#countdown(10)

#####################################################################
def summe(n):
    if n == 0:
        return 0
    else:
        return n + summe(n - 1)


print(summe(1))
print(summe(2))
print(summe(3))
print(summe(4))
print(summe(5))  # 15



