class Book:
    book_name:str
    author:str
    price:int
    pages:int

    def __init__(self,book_name,author,price,pages):
        self.book_name=book_name
        self.author=author
        self.price=price
        self.pages=pages

    def get(self):
        print(self.book_name,self.author,self.price)

    def __str__(self):
        return self.book_name


# __init__ => constructor

# obj=Book("DO EPIC SHIT","Ankur Warikoo",450,293) 
# print(obj.book_name)

obj1=Book("The Price","Alexandra",3645,288)
print(obj1) # __str__()
