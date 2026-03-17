class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name es {self.name} and I am {self.age}")


Person1 = Person("Ana",25)
Person1.greet()

class BankAccount:
    def __init__(self,account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
        
    def deposit(self,amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount}, Saldo actual {self.balance} COP")

        else:
            print("No se puede depositar, Cuenta inactiva")

    def withdraw(self,amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount}, Saldo actual {self.balance} COP")
    
    def deactivate(self):
        self.is_active = False
        print(f"La cuenta de {self.account_holder} ha sido desactivada")
    
    def activate_account(self):
        self.is_active = True
        print(f"La cuenta ha sido desactivada")


account1=BankAccount('Johany',500)
account2=BankAccount('Andres',400)
account1.deposit(200)
account1.deposit(100)
account1.deactivate()
account1.deposit(200)
account1.activate_account()
account1.deposit(200)  
                