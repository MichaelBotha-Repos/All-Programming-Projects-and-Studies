from abc import ABC, abstractmethod

class Abstract(ABC):
    @abstractmethod
    def interface(self):
        print("test123")


test = Abstract()