def add_euro_sign(amount):
    return f"€{amount}"


def get_deposit():
    min_amount = 1
    max_amount = 900

    while True:
        user_input = input(f"Please input deposit amount between {add_euro_sign(min_amount)} and {add_euro_sign(max_amount)}: ")
        # Trys to convert user_input to integer
        try: 
            deposit = int(user_input)
            # Checks if deposit amount is less than or equal to 0 or greater than (max_amount)
            # If the amount is less than equal to 0 or greater than (max_amount) it will loop back to the beginning and ask the user to input a valid amount
            if deposit <= 0 or deposit > max_amount: 
                print(f"Amount must be a number between {add_euro_sign(min_amount)} and {add_euro_sign(max_amount)}\n")
                continue
            # if inputted amount is valid it will return this amount. 
            return deposit
        except:
            print("Amount entered must a valid number\n") 
            continue


def get_bet(balance): 
    min_amount = 1

    while True:
        user_input = input(f"\nPlease enter the amount you wish to bet between {add_euro_sign(min_amount)} and {add_euro_sign(balance)}: ")
        
        try:
            bet_amount = int(user_input) 

            if bet_amount < min_amount:
                print(f"\nMinimum betting amount is equal to {add_euro_sign(min_amount)}")
                continue

            if bet_amount > balance:
                print(f"\nYour balance ({add_euro_sign(balance)}) is not sufficient to bet {add_euro_sign(bet_amount)}")
                continue
                
            return bet_amount
        except:
            print("\nAmount entered must a valid number")
            continue


def get_symbols():
    # This is a dictionary of Keys and Values 
    symbols = {
        "A": 3,
        "B": 6,
        "C": 9,
        "D": 12
    }

    all_symbols = []
    # Loop through dictionary symbols of keys(symbol) and values(count)
    for symbol, count in symbols.items():
        # Extending all symbols array
        # ["A"] * 3 = ["A", "A", "A"] for reference: https://note.nkmk.me/en/python-list-initialize/
        all_symbols.extend([symbol] * count)

    return all_symbols
    

def main(): 
    # Assigning a return value of function "get_deposit" to variable called "deposit" 
    deposit = get_deposit()
    balance = deposit
    all_symbols = get_symbols()

    while True:    
        # Take input, convert to lowercase then assign it to variable called user_input
        user_input = input("\nPress Enter to play or Q to quit: ").lower()
        # if the user will input Q or q game will end
        if user_input == "q": 
            print("\nThank you for playing, see you again soon!")
            break

        print(f"\nYour balance is €{balance}")

        bet = get_bet(balance)

        
main()