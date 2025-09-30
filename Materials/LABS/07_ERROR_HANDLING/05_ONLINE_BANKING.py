class MoneyNotEnoughError(Exception):
    pass

class PINCodeError(Exception):
    pass

class UnderageTransactionError(Exception):
    pass 

class MoneyIsNegativeError(Exception):
    pass

MIN_AGE = 18

pin,balance,age = [int(x) for x in input().split(", ")]

while (transaction := input()) != 'End':

    transaction_info = transaction.split('#')

    if transaction_info[0] == 'Send Money':

        if age < MIN_AGE:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")
        
        try:
            money,trans_pin = map(int,transaction_info[1:])
        except ValueError:
            print('One or more parameters is missing')
        
        else:  
            if pin != trans_pin:
                raise PINCodeError("Invalid PIN code")
            
            if money > balance:
                raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
        
            balance -= money
            print(f"Successfully sent {money:.2f} money to a friend")
            print(f"There is {balance:.2f} money left in the bank account")
        
    elif transaction_info[0] == 'Receive Money':
        try:
            amount = int(transaction_info[1])
        except ValueError:
            print('Amount missing')

        else:
            if amount < 0:
                raise MoneyIsNegativeError("The amount of money cannot be a negative number")
    
            amount = amount /2
            print(f"{amount:.2f} money went straight into the bank account")


