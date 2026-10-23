class Transaction():
    """
    A class to represent a financial transaction with an ID, amount, region, and date.
    """
 
    # Initializes a new Transaction instance with the given ID, amount, region, and date.
    def __init__(self, id, amount, region, date):
        self._id = id
        self._amount = amount
        self.region = region
        self.date = date

    # Returns a string representation of the transaction details. 
    def __str__(self):
        return f"[{self._id}] Amount: {self._amount} | Region: {self.region} | Date: {self.date}"

    # Returns a formatted string containing the transaction's ID, amount, region, and date.
    def get_details(self):
        return f"[{self._id}] Amount: {self._amount} | Region: {self.region} | Date: {self.date}"


transaction1 = Transaction(1, 100.0, "North America", "2023-01-01")

print(transaction1.get_details())

# Define InternationalTransaction that inherits from Transaction.
class InternationalTransaction(Transaction):
    
    '''A class to represent an international financial transaction with a currency.'''
    def __init__(self, id, amount, region, date, currency):

        super().__init__(id, amount, region, date)

        self.currency = currency
    
    # Returns a formatted string containing the transaction's details including currency.
    def get_details(self):
        base_details = super().get_details()
        return f"[{base_details} | Currency: {self.currency}"

import json

class DataLoader():
    """
    A class to load transaction data from a CSV file.
    """

    def __init__(self, file_path):
        
        self.file_path = file_path
        self.transactions = []

    # Validates that the amount is a float and greater than zero.
    @staticmethod
    def validate_amount(amount):
        return amount > 0

    def load_transactions(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                amount = line.get('amount', 0)
                if not DataLoader.validate_amount(amount):
                    raise ValueError(f"Invalid amount: {amount}. Amount must be greater than zero.")
                    continue
                
                if 'currency' in line:
                    transaction = InternationalTransaction(
                        line['id'], float(amount), line['region'], line['date'], line['currency']
                    )
                else:
                    transaction = Transaction(
                        line['id'], float(amount), line['region'], line['date']
                    )
                self.transactions.append(transaction)
            return self.transactions

    def get_transactions(self):
        return self.transactions
    
# Demonstrate in __main__ that calling get_details() on an InternationalTransaction instance returns the extended string.
if __name__ == "__main__":
    # create a sample of transaction data
    international_transaction = InternationalTransaction(2, 200.0, "Europe", "2023-02-01", "EUR")
    
    loader = DataLoader("processed_data.txt")
    loader.load_transactions()
    
    for tx in loader.get_transactions():
        print(tx.get_details())
    
    print(international_transaction.get_details())
    
    val_negative = DataLoader.validate_amount(-50)
    val_positive = DataLoader.validate_amount(120)
    print(f"DataLoader.validate_amount(-50): {val_negative}")
    print(f"DataLoader.validate_amount(120): {val_positive}")



    