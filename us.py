# Simple ATM Program in Python
user = {'pin': 1234, 'balance': 1000}

def withdraw_cash():
    while True:
        amount = int(input("Enter the amount of money you want to withdraw: "))
        if amount > user['balance']:
            print("You don't have sufficient balance to make this withdrawal")
        else:
            user['balance'] -= amount
            print(f"{amount} Rupees successfully withdrawn. Your remaining balance is {user['balance']} Rupees")
            print('')
            return False

def balance_enquiry():
    print(f"Total balance: {user['balance']} Rupees")
    print('')

print("Welcome to the Python ATM")
pin = int(input('Please enter your four-digit PIN: '))

if pin == user['pin']:
    while True:
        print("What do you want to do?")
        print("1. Withdraw Cash\n2. Balance Enquiry\n3. Quit")
        query = int(input("Enter the number corresponding to the activity you want to do: "))
        if query == 1:
            withdraw_cash()
        elif query == 2:
            balance_enquiry()
        elif query == 3:
            break
        else:
            print("Please enter a correct value shown")
else:
    print("Entered wrong PIN")
