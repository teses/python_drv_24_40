"""
    Interface mit @abstractmethod simulieren

"""
from abc import ABC, abstractmethod

# Interface durch abstract
class LoggerInterface(ABC):

    @abstractmethod
    def log(self):
        pass


class User():

    def __init__(self, name):
        self.name = name



class Person(User, LoggerInterface):

    def __init__(self, name):
        self.name = name

    #def log(self):
    #    print("log....")

p = Person("Max")
p.log()


