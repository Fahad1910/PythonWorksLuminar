from abc import ABC,abstractmethod                 #ABC-abstract base class

class Bike(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def breaks(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

class Hunter(Bike):
    
    def start(self):
        print("Hunter starts")

    def accelerate(self):
        print("hunter accelerate")

    def breaks(self):
        print("hunter break")

obj=Hunter()
obj.start()
obj.accelerate()