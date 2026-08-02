from abc import ABC, abstractmethod

# Abstract base class representing the Strategy interface for payments
class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


# Concrete strategy for processing payments via Credit Card
class CreditCardPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"₹{amount} paid using Credit Card.")


# Concrete strategy for processing payments via Debit Card
class DebitCardPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"₹{amount} paid using Debit Card.")


# Concrete strategy for processing payments via UPI
class UPIPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"₹{amount} paid using UPI.")


# Concrete strategy for processing payments via Net Banking
class NetBankingPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"₹{amount} paid using Net Banking.")


# Context class that uses a PaymentStrategy to execute payments
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    # Getter property to retrieve the current payment strategy
    @property
    def strategy(self):
        return self._strategy

    # Setter property to dynamically change the payment strategy at runtime
    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    # Executes the payment using the configured strategy
    def pay(self, amount):
        self._strategy.process_payment(amount)


def main():
    # Prompt the user to enter the payment amount
    amount = float(input("Enter payment amount: "))

    # Display available payment options
    print("\nSelect Payment Method")
    print("1. Credit Card")
    print("2. Debit Card")
    print("3. UPI")
    print("4. Net Banking")

    # Get the user's choice of payment method
    choice = int(input("Enter your choice: "))

    # Map user choices to their respective concrete strategy objects
    strategies = {
        1: CreditCardPayment(),
        2: DebitCardPayment(),
        3: UPIPayment(),
        4: NetBankingPayment()
    }

    # Retrieve the selected strategy from the dictionary
    strategy = strategies.get(choice)

    # If a valid strategy is chosen, initialize the processor and execute payment
    if strategy:
        processor = PaymentProcessor(strategy)
        processor.pay(amount)
    else:
        print("Invalid Payment Method!")


if __name__ == "__main__":
    main()