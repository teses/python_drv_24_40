

class Countdown:

    def __init__(self, start):
        self.counter = start
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter <= 0:
            raise StopIteration

        val = self.counter
        self.counter -= 1
        return val


########################################################################
countdownIterator = iter(Countdown(5))

print(next(countdownIterator))
print(next(countdownIterator))
print(next(countdownIterator))
print(next(countdownIterator))
print(next(countdownIterator))
#print(next(countdownIterator)) # StopIteration


# Implementierung mit for
print("-"*50)
for num in Countdown(5):
    print(num)