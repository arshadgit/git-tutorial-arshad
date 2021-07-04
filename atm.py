pin=5432
balance=100000
print("Welcome to ARSHAD ATM")
pin=int(input("Enter your pin"))
if(pin==pin):
    amount=int(input("Enter the money to withdraw"))
    if(amount<=balance and amount%100==0):
        print("withdrawn successfully")
        remaining= balance-amount
        print("Remaining balance=",remaining)
    else:
        print("Invalid amount")
else:
    print("Invalid pin")



