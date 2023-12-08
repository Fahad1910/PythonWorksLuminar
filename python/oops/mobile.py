class Mobile:
  
    def __init__(self,*args,**kwargs):
        self.name=kwargs.get("name")
        self.brand=kwargs.get("brand")
        self.display=kwargs.get("display")

    def display_details(self):
        print(self.name,self.brand,self.display)


class Mobilevarient(Mobile):
    price=int
    color=str

    def __init__(self, *args, **kwargs):
        self.price=kwargs.pop("price")
        self.color=kwargs.pop("color")
        print(self.price,self.color)
        super().__init__(kwargs)

    def display(self):
        super(self).display_details()
        print(self.price,self.color)

mv=Mobilevarient(name="milli",brand="mi",display="amoled",price=12000,color="grey")