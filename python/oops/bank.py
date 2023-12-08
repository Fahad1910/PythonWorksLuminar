class Bank:
    ac_no:int
    person_name:str
    ifsc_code:str
    branch:str
    ac_type:str
    balance:int
    bank_name:str
    
    def create(self,acc_no,person_name,ifsc_code,branch,acc_type,balance,bank_name):
        self.ac_no=acc_no
        self.person_name=person_name
        self.ifsc_code=ifsc_code
        self.branch=branch
        self.ac_type=acc_type
        self.balance=balance
        self.bank_name=bank_name


    def deposit(self,amount):
        self.balance+=amount
        print(f"your {self.bank_name} account has been credited with ammount {amount} aval bal {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance Transaction declined")
        else:
            self.balance-=amount
            print(f"your {self.bank_name} account has been debited with ammount {amount} aval bal {self.balance}")

    def get_balance(self):
        print(f"your aval balance {self.balance}")


obj=Bank()
obj.create(456128,"Fahad","UBIN0075","Aluva","Savings",65000,"UBI")


obj.deposit(10000)
obj.withdraw(5000)
obj.get_balance()

