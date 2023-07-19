import random

SYMBOLS_IN_WINNING_LINE = 3
SYMBOLS = {
    "A": {
        "count": 3,
        "value": 5
    },
     "B": {
        "count": 6,
        "value": 4
    },
    "C": {
        "count": 9,
        "value": 3
    },
    "D": {
        "count": 12,
        "value": 2
    }
}

def add_euro_sign(amount):
    return f"€{amount}"


def print_separator_line():
    print("\n--------------------------------------------------------------------")


def print_win_or_loss(winnings, balance):
    if winnings > 0:
        print(f"\nYou won! Your balance is now {add_euro_sign(balance)}")
    else:
        print(f"\nYou lost... Your balance is now {add_euro_sign(balance)}")


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
    all_symbols = []
    # Loop through dictionary symbols of keys(symbol) and values(count and symbol value) nested inside SYMBOLS dictionary
    for symbol, values in SYMBOLS.items():
        # Extending all symbols array
        # ["A"] * 3 = ["A", "A", "A"] for reference: https://note.nkmk.me/en/python-list-initialize/
        all_symbols.extend([symbol] * values["count"])

    return all_symbols


# This all_symbols is not referring to the array in above function
def get_winning_line(all_symbols):
    return random.sample(all_symbols, SYMBOLS_IN_WINNING_LINE)


def print_winning_line(winning_line):
    print()
    print(" | ".join(winning_line))


# (Winning_line) is a list of elements 
def calculate_winnings(winning_line, bet):
    #symbol is defined by first_element
    first_element = winning_line[0]
    winnings = 0

    for symbol in winning_line:
        if first_element != symbol:
            break
    else: 
        symbol_multiplier = SYMBOLS[first_element]["value"]
        winnings = symbol_multiplier * bet

    return winnings


def spin(bet, symbols):
    winning_line = get_winning_line(symbols)
    
    print_winning_line(winning_line)
    
    winnings = calculate_winnings(winning_line, bet)

    return winnings - bet


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

        print(f"\nYour balance is {add_euro_sign(balance)}")

        bet = get_bet(balance)
        winnings = spin(bet, all_symbols)
        balance += winnings

        print_separator_line()
        print_win_or_loss(winnings, balance)
        print_separator_line()
    
        
main()