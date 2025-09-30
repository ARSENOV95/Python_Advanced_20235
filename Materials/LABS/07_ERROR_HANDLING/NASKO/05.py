class MoneyNotEnoughError(Exception):
    pass

class PINCodeError(Exception):
    pass

class UnderageTransactionError(Exception):
    pass 

class MoneyIsNegativeError(Exception):
    pass


pin,balance,age = map(int,input().split(", "))

MIN_AGE = 18

while True:
    command = input().split('#')

    if command[0] == 'End':
        break

    if command[0] == "Send Money":
        money,given_pin = map(int,command[1:])
        
        if money > balance:
            raise MoneyNotEnoughError
        
        if given_pin != pin:
            raise PINCodeError
        
        if age < MIN_AGE:
            raise UnderageTransactionError

        balance -= money
        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")

        
    elif command[0] == "Receive Money":
        money = int(command[1])
        if money < 0:
            raise MoneyIsNegativeError
        
        balance += money/2
        print(f'{money/2:.2f} money went straight into the bank account')
