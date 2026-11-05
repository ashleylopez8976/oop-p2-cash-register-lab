#!/usr/bin/env python3

    # Initialize the discount, total, items, and transaction history.
class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []
    
     # Add the purchase to the total and record it for later reversal.
    def add_item(self, item, price, quantity=1):
        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })
    
    # Apply the percentage discount to the current total.
    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total -= self.total * (self.discount / 100)
            print(f"After the discount, the total comes to ${self.total:g}.")

    # Undo the most recent purchase and remove its items.
    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        transaction = self.previous_transactions.pop()

        self.total = round(
            self.total - transaction["price"] * transaction["quantity"],
            2
        )

        for _ in range(transaction["quantity"]):
            self.items.pop()

    @property
    def discount(self):
        return self._discount

    # Allow only integer discounts from 0 through 100.
    @discount.setter
    def discount(self, value):
        if type(value) is int and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")