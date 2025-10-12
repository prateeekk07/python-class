from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def airbags(self):
        pass

class TATA(Car):
    def airbags(self):
        print("5 star rating")

nexon = TATA()
nexon.airbags()
