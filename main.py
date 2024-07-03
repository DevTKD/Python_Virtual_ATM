from user_authentication import user_authenticated
from atm_functions import atm_terminal

print("Welcome to Davis Bank")
print()

if user_authenticated():
    atm_terminal()
