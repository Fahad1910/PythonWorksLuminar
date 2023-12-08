class Parent:
    phone="Redmi 9"
    bike="Passion pro"

    def mobile(self):
        print(self.phone)

    def vehicle(self):
        print(self.bike)

class Child(Parent):
    pass

obj=Child()
obj.mobile()