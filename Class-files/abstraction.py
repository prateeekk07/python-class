from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def airbags(self):
        pass

    @abstractmethod
    def safety_sensor(self):
        pass

    @abstractmethod
    def steering(self):
        pass

    @abstractmethod
    def wheels(self):
        pass

    @abstractmethod
    def engine(self):
        pass

    @abstractmethod
    def ncap_rating(self):
        pass

# from functools import reduce
# from math import pi
# object

class Tata(Car):
    def airbags(self):
        print("6 airbags")

    def safety_sensor(self):
        print("12 sensors")

    def steering(self):
        print("power steering")

    def wheels(self):
        print("5 alloy wheels")

    def engine(self):
        print("1600 cc BS6")

    def ncap_rating(self):
        print("ncap rating 5")

    def sunroof(self):
        print("panaromic sunroof")

# nexon = Tata()
# nexon.ncap_rating()




class Hyundai(Car):
    pass


class BMW(Car):
    pass

class MarutiSuzuki(Car):
    pass


class Common(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

class WriteFile(ABC):
    @abstractmethod
    def write(self):
        pass


class ReadonlyFile(Common):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

# obj = ReadonlyFile()


class PDFFile(WriteFile, Common):
    def open(self):
        print("opening pdf file")

    def read(self):
        print("reading pdf file")

    def close(self):
        print("closing pdf file")


# class ExcelFile(File):
#     def open(self):
#         print("opening excel file")

#     def read(self):
#         print("reading excel file")

#     def close(self):
#         print("closing excel file")

# class TextFile(File):
#     def open(self):
#         print("opening text file")

#     def read(self):
#         print("reading text file")

#     def close(self):
#         print("closing text file")

# class CSVFile(File):
#     def open(self):
#         print("opening csv file")

#     def read(self):
#         print("reading csv file")

#     def close(self):
#         print("closing csv file")


# def file_operation():
#     user_inp = input('Enter class name:- ')
#     class_name = globals()[user_inp] # CSVFile <class '__main__.CSVFile'>
#     obj = class_name() # CSVFile()
#     obj.open()
#     obj.read()
#     obj.close()

# file_operation()
# lst = [TextFile(), PDFFile(), ExcelFile(), CSVFile()]
# for file_obj in lst:
#     file_operation(file_obj)

from abc import ABC, abstractmethod

# Define an interface
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        """Process a payment of the given amount."""
        pass

    @abstractmethod
    def refund(self, amount):
        """Refund a payment of the given amount."""
        pass

# Implementing the interface
class PayPalGateway(PaymentGateway):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")

    def refund(self, amount):
        print(f"Refunded ₹{amount} using PayPal")

class StripeGateway(PaymentGateway):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Stripe")

    def refund(self, amount):
        print(f"Refunded ₹{amount} using Stripe")

# Usage
# gateway = PayPalGateway()
# gateway.pay(500)
# gateway.refund(200)

# gateway = StripeGateway()
# gateway.pay(700)
# gateway.refund(100)


from typing import Protocol

class PaymentGateway(Protocol):
    def pay(self, amount: float) -> None: ...
    def refund(self, amount: float) -> None: ...

# No inheritance required:
class Razorpay:
    def pay(self, amount: float) -> None:
        print(f"Paid ₹{amount} via Razorpay")

    def refund(self, amount: float) -> None:
        print(f"Refunded ₹{amount} via Razorpay")

# def process_payment(gateway: PaymentGateway, amount: float) -> None:
#     gateway.pay(amount)

# razorpay = Razorpay()
# process_payment(razorpay, 1000)  # Works because Razorpay matches the Protocol

# What is SOLID principle? purpose?
# explain Interface Sagregation with example




from abc import ABC, abstractmethod

class Machine(ABC):
    @abstractmethod
    def print_document(self, doc): pass

    @abstractmethod
    def scan_document(self, doc): pass

    @abstractmethod
    def fax_document(self, doc): pass

# OldPrinter only prints, but is forced to implement all methods
class OldPrinter(Machine):
    def print_document(self, doc):
        print("Printing:", doc)

# obj = OldPrinter()
# obj.print_document("salary file")

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self, doc): pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self, doc): pass

class Fax(ABC):
    @abstractmethod
    def fax_document(self, doc): pass

# Simple printer implements only what it needs
class SimplePrinter(Printer):
    def print_document(self, doc):
        print("Printing:", doc)

# Multi-function printer implements all three interfaces separately
class MultiFunctionDevice(Printer, Scanner, Fax):
    def print_document(self, doc):
        print("Printing:", doc)

    def scan_document(self, doc):
        print("Scanning:", doc)


from abc import ABC, abstractmethod

class PaymentService(ABC):
    @abstractmethod
    def pay_credit_card(self, amount: float): pass

    @abstractmethod
    def pay_debit_card(self, amount: float): pass

    @abstractmethod
    def pay_upi(self, amount: float): pass

    @abstractmethod
    def pay_crypto(self, amount: float): pass

# Vendor only supports UPI but is forced to implement all
class UpiVendor(PaymentService):
    def pay_credit_card(self, amount: float):
        raise NotImplementedError("Credit card not supported")

    def pay_debit_card(self, amount: float):
        raise NotImplementedError("Debit card not supported")

    def pay_upi(self, amount: float):
        print(f"Paid ₹{amount} via UPI")

    def pay_crypto(self, amount: float):
        raise NotImplementedError("Crypto not supported")

from abc import ABC, abstractmethod

class CreditCardPayment(ABC):
    @abstractmethod
    def pay_credit_card(self, amount: float): pass

class DebitCardPayment(ABC):
    @abstractmethod
    def pay_debit_card(self, amount: float): pass

class UpiPayment(ABC):
    @abstractmethod
    def pay_upi(self, amount: float): pass

class CryptoPayment(ABC):
    @abstractmethod
    def pay_crypto(self, amount: float): pass


# Vendor now implements only what it supports
class UpiVendor(UpiPayment):
    def pay_upi(self, amount: float):
        print(f"Paid ₹{amount} via UPI")

# Another vendor supports credit card and crypto
class CardAndCryptoVendor(CreditCardPayment, CryptoPayment):
    def pay_credit_card(self, amount: float):
        print(f"Paid ₹{amount} via Credit Card")

    def pay_crypto(self, amount: float):
        print(f"Paid ₹{amount} via Crypto")

