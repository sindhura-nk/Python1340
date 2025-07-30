from abc import ABC,abstractmethod

# Abstract class can have abstract method and also generic methods
class Animal(ABC):
    # if needed, you can have init here
    def __init__(self):
        super().__init__()
    # abstract method
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def __init__(self,breed):
        super().__init__()
        self.breed = breed
    def make_sound(self):
        print(f"Dog barks.")
    def qualities(self):
        print(f"Dog belongs to {self.breed}")

class Cat(Animal):
    pass

d1 = Dog("Golden Retriever")
#d1.qualities()
d1.make_sound()

## Create a Payment related Abstract Class. Credit/Debit Card, UPI,Net Banking
class paymentProcessor(ABC):
    def __init__(self):
        super().__init__()
    @abstractmethod    
    def pay(self):
        print("Proceed with the payment")
    def greeting(self):
        print("Welcome to our application")

class CreditCard(paymentProcessor):
    pass
class NetBanking(paymentProcessor):
    pass

data = ["23423432@hdfc","32432324@axis","345435345@sbi"]
class UPI(paymentProcessor):
    
    def __init__(self,upi_id):
        super().__init__()
        self.upi_id = upi_id
    def pay(self):
        print("Payment Process has started")
        self.validate_upi_id()
        self.deduct_amount()
        print("Payment is successful.Order is placed.")
    def bank_server_connectivity(self):
        print("Bank server connection successful")
    def validate_upi_id(self):
        #code for validation
        if self.upi_id in data:
            self.bank_server_connectivity()
        else:
            print("Payment Unsuccessful due to incorrect UPI ID")
    def deduct_amount(self):
        print("Payment Successful. Reverting back to Portal. Donot refresh the screen")
upi_1 = UPI("23423432@hdfc")
upi_1.pay()
upi_2 = UPI("23424")
upi_2.pay()
# as a coder, you will be able to view other methods, however, the end user will not be able to view other methods
# any method other than abstract methods,will not be visible for the end user.
