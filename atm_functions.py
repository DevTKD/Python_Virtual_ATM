from inputimeout import inputimeout, TimeoutOccurred

# ATM Functions
account_balance = float(100.00)


def check_balance():
    global account_balance
    print(f"Your current balance is: ${account_balance:.2f}")
    log_transaction(f"Check Balance: ${account_balance:.2f}")


def deposit():
    global account_balance
    print("Enter the deposit amount or type 'cancel' to return to the main menu.")
    while True:
        # Now we expect either an amount or 'cancel'
        user_input = input("Amount ($): ").strip().lower()

        if user_input == 'cancel':  # Check if the user wants to cancel the deposit
            print("Deposit cancelled. Returning to the main menu.")
            return  # Exit the function and go back to the main menu

        try:
            deposit_amount = float(user_input)

            if deposit_amount <= 0:
                print("Invalid amount. Please enter a positive amount.")
                continue

        except ValueError:
            print("Invalid input. Please enter a valid dollar amount or 'cancel'.")
            continue

        account_balance += deposit_amount
        print(f"${deposit_amount:.2f} deposited successfully.")
        print(f"Your new account balance is ${account_balance:.2f}")
        log_transaction(f"Deposit: ${deposit_amount:.2f}")
        break


def withdrawal():
    global account_balance
    print("Enter the withdrawal amount or type 'cancel' to return to the main menu.")
    while True:
        user_input = input("Amount ($): ").strip().lower()

        if user_input == 'cancel':
            print("Withdrawal cancelled. Returning to the main menu.")
            return

        try:
            withdrawal_amount = float(user_input)

            if withdrawal_amount <= 0:
                print("Invalid amount. Please enter a positive amount.")
                continue

        except ValueError:
            print("Invalid input. Please enter a valid dollar amount or 'cancel'.")
            continue

        if withdrawal_amount <= account_balance:
            account_balance -= withdrawal_amount
            print(f"${withdrawal_amount:.2f} withdrawn successfully.")
            print(f"Your updated account balance is ${account_balance:.2f}")
            log_transaction(f"Withdrawal: ${withdrawal_amount:.2f}")
            break
        else:
            print("Insufficient funds for this withdrawal.")
            log_transaction(
                f"Insufficient funds for withdrawal attempt: ${withdrawal_amount:.2f}")
            break


# Initialize a global list to store transaction logs
transaction_log = []


def log_transaction(transaction):
    transaction_log.append(transaction)

# Display the five most recent transactions, or all transactions if fewer than five exist


def view_recent_transactions():
    print("Recent transactions:")
    for transaction in transaction_log[-5:]:
        print(transaction)


def atm_terminal():
    print("Welcome to the Virtual ATM!")
    input_timeout = 30  # Timeout for input in seconds

    while True:
        try:
            print("\nSelect an option:")
            print("1. Check Balance")
            print("2. Make a Deposit")
            print("3. Make a Withdrawal")
            print("4. View Recent Transactions")
            print("5. Exit")
            choice = inputimeout(prompt="Your choice: ", timeout=input_timeout)
        except TimeoutOccurred:
            print(
                "Timeout occurred: No activity for 30 seconds. Exiting the Virtual ATM.")
            break  # Exit the while loop to end the ATM session

        if choice == '1':
            check_balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdrawal()
        elif choice == '4':
            view_recent_transactions()
        elif choice == '5':
            print("Thank you for using the Virtual ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
