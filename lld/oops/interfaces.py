"""

An Interface is basically like an contract , a list of methods , that any implementing class from that parent class must define adn provide.


An interface defines the "what", while classes provide the "how".


In Python interfaces are implemented via abstrac classes.

An abstract class is like a template for other classes.
It defines methods that must be included in any class that inherits from it, but it doesn’t provide the actual code for those methods.
"""

# Payment Gateway Interface

from abc import ABC, abstractmethod


class PaymentGateway(ABC):

    @abstractmethod
    def initiate_payment(self, amount):
        pass


class RazorPay(PaymentGateway):
    def initiate_payment(self, amount):
        print(f"Processing Payment Via Razorpay {amount}")


class Stripe(PaymentGateway):
    def initiate_payment(self, amount):
        print(f"Processing Payment Via Stripe {amount}")


class CheckOutService:
    def __init__(self, payment_gateway) -> None:
        self.payment_gateway = payment_gateway

    def set_payment_gateway(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def checkout(self, amount):
        self.payment_gateway.initiate_payment(amount)


razorpay_gateway = RazorPay()

razoray_checkout = CheckOutService(razorpay_gateway)

razoray_checkout.checkout(amount=5000)


stripe_gateway = Stripe()

stripe_checkout = CheckOutService(stripe_gateway)

stripe_checkout.checkout(amount=5000)
