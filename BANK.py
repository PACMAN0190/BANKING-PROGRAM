def show_balance(balance):
    print("********************************")
    print(f"Your balance is: ${balance:.2f}")
    print("********************************")


def deposits():
    print("********************************")
    try:
        amount = float(input("Enter amount to deposit: "))
    except ValueError:
        print("invalid input")
        print("********************************")
        return 0
    print("********************************")

    if amount <= 0:
        print("invalid amount")
        print("********************************")
        return 0
    else:
        return amount


def withdraws(balance):
    try:
        amount = float(input("Enter amount to withdraw: "))
    except ValueError:
        print("********************************")
        print("invalid input")
        print("********************************")
        return 0

    if amount > balance:
        print("********************************")
        print("insufficient balance")
        print("********************************")
        return 0
    elif amount <= 0:
        print("********************************")
        print("invalid amount")
        print("********************************")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("********************************")
        print("banking program")
        print("********************************")
        print("1. show balance")
        print("2. deposit")
        print("3. withdraw")
        print("4. exit")
        print("********************************")

        choice = input("Enter your choice (1 - 4): ")

        if choice == "1":
            show_balance(balance)

        elif choice == "2":
            balance += deposits()

        elif choice == "3":
            balance -= withdraws(balance)

        elif choice == "4":
            is_running = False

        else:
            print("********************************")
            print("invalid choice")
            print("********************************")

    print("********************************")
    print("Thank you! Have a good day 😁")
    print("********************************")


if __name__ == "__main__":
    main()
