class Parent:
    
    props=["Passion pro","Swift"]

    def get_properties(self):
        return self.props
    
class Child(Parent):
    
    def get_properties(self):
        self.p=super().get_properties()
        self.p.append("hunter")
        return self.p
    
ch=Child()
print(ch.get_properties())


# super() is used to refer the parent class