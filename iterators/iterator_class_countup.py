

class Countup:

    def __init__(self, start, to):
        self.counter = start
        self.to = to
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >  self.to:
            raise StopIteration

        val = self.counter
        self.counter += 1
        return val


########################################################################
CountupIterator = iter(Countup(1, 10))

print(next(CountupIterator))
print(next(CountupIterator))
print(next(CountupIterator))
print(next(CountupIterator))
print(next(CountupIterator))


# Implementierung mit for
print("-"*50)
for num in Countup(1,10):
    print(num)