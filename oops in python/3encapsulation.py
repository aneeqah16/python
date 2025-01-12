# encapsulation: hiding implementation details

class test:

    def __init__(self,a,b):
        self.a = a
        self.b = b

t = test(4,6)
print(t.a)
# we can reassign the value of t.a
t.a = 67565
print(t.a)

# how can we hide this so no one can manuplate the data?

class car:
    def __init__(self,year,make,model,speed):
        self.__year = year
        # __ makes a variable private
        # compiler will hide this data from the user
        self.__make = make
        self.__model = model
        self.__speed = 0
    # custom method to set speed
    def set_speed(self,speed):
        self.__speed = 0 if speed < 0 else speed
    # custom method to show speed
    def get_speed(self):
        return self.__speed

c = car(2023,"toyata","innova","120") 
print(c._car__year ) 
# wont be accessed directly
c.set_speed(5656)
print(c.get_speed())

class bank_account:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,amount):
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print("transaction successful")
            return True
        else:
            print("not sufficient balance")
            return False
    def get_balance(self):
        return self.__balance
    
anee = bank_account(746545)
print(anee.get_balance())
# print(anee.bank_account__balance)
anee.deposit(7854778886)
print(anee.get_balance())

anee.deposit(1000)
print(anee.get_balance())

anee.withdraw(2000)
print(anee.get_balance())


        