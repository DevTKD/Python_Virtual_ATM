from inputimeout import inputimeout, TimeoutOccurred

# user authentication function

correct_account_number = "123456789"
correct_account_PIN = "9551"


def user_authenticated():
    account_number = ""
    account_PIN = ""

    account_attempts = 0
    pin_attempts = 0
    max_attempts = 3  # Maximum number of attempts allowed
    input_timeout = 30  # Timeout for input in seconds

    while account_attempts < max_attempts:
        try:
            account_number = inputimeout(
                prompt="Enter your 9 digit account number: ", timeout=input_timeout)
        except TimeoutOccurred:
            print(
                "Timeout occurred: You did not enter your account number within 30 seconds.")
            return False

        if len(account_number) == 9 and account_number.isdigit():
            break
        else:
            account_attempts += 1
            print("Invalid account number format. Please enter a 9-digit account number.")
            print(f"Attempt {account_attempts} of {max_attempts}")

            if account_attempts == max_attempts:
                print("Error: Too many incorrect attempts. Access denied.")
                return False

    while pin_attempts < max_attempts:
        try:
            account_PIN = inputimeout(
                prompt="Enter your PIN: ", timeout=input_timeout)
        except TimeoutOccurred:
            print("Timeout occurred: You did not enter your PIN within 30 seconds.")
            return False

        if 4 <= len(account_PIN) <= 6 and account_PIN.isdigit():
            if account_number == correct_account_number and account_PIN == correct_account_PIN:
                return True
            else:
                pin_attempts += 1
                print(
                    f"Authentication failed. Incorrect PIN. Attempt {pin_attempts} of {max_attempts}")
                if pin_attempts == max_attempts:
                    print("Error: Too many incorrect attempts. Access denied.")
                    return False
        else:
            pin_attempts += 1
            print("Invalid PIN format. Please enter a 4-6 digit PIN.")
            print(f"Attempt {pin_attempts} of {max_attempts}")
