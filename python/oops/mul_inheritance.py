class P1:
    def m1(self):
        print("inside class p1 m1 method")

class P2:
    def m2(self):
        print("inside class p2 m2 method")

class Child(P2,P1):
    def m3(self):
        print("inside the class Child m3 method")

obj=Child()
obj.m3()
obj.m2()
obj.m1()    


# polymorphism - many forms
#      > method overriding
#      > method overloading


