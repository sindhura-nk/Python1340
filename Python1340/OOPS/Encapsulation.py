# import necessary libraries and classes
from abc import ABC,abstractmethod

class bank_details:
    def __init__(self,account_number):
        self._account_number = account_number
    def validate(self):
        #user account details authentication
        print("User authentication successful")
    def balance(self):
        print("Your balance is ",65000)

print("===================")
print("Protected usecase output")
user1 = bank_details(23423432423)
user1.validate()
user1.balance()
print(user1._account_number)

class bank_updated_balance:
    def __init__(self,balance):
        self.__balance = balance
    def updated_balance(self):
        self.__balance = self.__balance - 15000
        print(f"Updated balance is {self.__balance}")

print("==================")
print("Private scenario output: ")
user2 = bank_updated_balance(89000)
user2.updated_balance()
#print(user2.__balance)

## Create a Payment related Abstract Class. Credit/Debit Card, UPI,Net Banking
class paymentProcessor(ABC):
    def __init__(self):
        super().__init__()
    @abstractmethod    
    def pay(self):
        print("Proceed with the payment")
    def greeting(self):
        print("Welcome to our application")

data = ["23423432@hdfc","32432324@axis","345435345@sbi"]
class UPI(paymentProcessor):
    
    def __init__(self,upi_id):
        super().__init__()
        self._upi_id = upi_id
    def pay(self):
        print("Payment Process has started")
        self.__validate_upi_id()
        self.__deduct_amount()
        print("Payment is successful.Order is placed.")
    def __bank_server_connectivity(self):
        print("Bank server connection successful")
    def __validate_upi_id(self):
        #code for validation
        if self._upi_id in data:
            self.__bank_server_connectivity()
        else:
            print("Payment Unsuccessful due to incorrect UPI ID")
    def __deduct_amount(self):
        print("Payment Successful. Reverting back to Portal. Donot refresh the screen")
    
upi_1 = UPI("23423432@hdfc")
upi_1.pay()
upi_1.__bank_server_connectivity()
upi_1.__deduct_amount()
upi_2 = UPI("23424")
upi_2.pay()

'''
Practice scenario:
ATM Machine.
We are providing Card Number, PIN
withdrawal
check balance
deposit
define card number, pin as protected variables/attributes
define the above 3 methods as abtract methods
'''