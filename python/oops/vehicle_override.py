class Car:
    def start(self):
        print("Key start")

    def break_type(self):
        print("Drum break")

    def transmission(self):
        print("Manual")

class Ambassador(Car): # Ambassador is a car
    pass

class Maruthi800(Car):
    def break_type(self):
        print("Disc break")

class BMW(Car):
    def start(self):
        print("SSB")

    def break_type(self):
        print("ABS")

    def transmission(self):
        print("Automatic")

obj=Ambassador()
obj.start()

obj1=Maruthi800()
obj1.break_type()

obj2=BMW()
obj2.transmission()

