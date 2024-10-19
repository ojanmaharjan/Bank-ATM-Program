def show_balance(balance):
    print(f"The Balance is :RS {balance}")
    return 0
    
def deposit(balance):
    amount = float(input(f"Enter the amount you want to deposite: RS"))
    if amount < 0:
        print("Not Valid")
        return 0
    else:
        print(f"Sucessful deposite: RS{amount}.")
        return amount
def withdraw(balance):
    amount = float(input(f"Enter the amount to withdraw: "))
    if balance <amount:
        print(f"Insufficient Balance")
        return 0
    elif amount <= 0:
        print("Amount must be greater than 0")
        return 0
    else:
        print(f"Withdraw sucessful: RS{amount}.")
        return amount

def main():
    start = True
    balance = 0

    while start:
        print("Banking Program")
        print("1.Show Balance")
        print("2.Deposit Money")
        print("3.Withdraw Money")
        print("4.Exit")

    
        choice =float(input("Enter your choice (1-4): "))
        if choice == 1:
            show_balance(balance)
            
        elif choice == 2:
            balance+=deposit(balance)
        elif choice ==3:
            balance -=withdraw(balance)
        elif choice ==4:
            start=False
        else:
            print("That is not a valid choice")
    print("Thank you for using the banking program!")

if __name__ == '__main__':
    main()


    





