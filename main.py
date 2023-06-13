def get_deposit():
    max_amount = 900
    
    while True:
        user_input = input(f"Please input deposit amount between €1 and {max_amount}: ")
        # Trys to convert user_input to integer
        try: 
            deposit = int(user_input)
            # Checks if deposit amount is less than or equal to 0 or greater than (max_amount)
            # If the amount is less than equal to 0 or greater than (max_amount) it will loop back to the beginning and ask the user to input a valid amount
            if deposit <= 0 or deposit > max_amount: 
                print(f"Amount must be a number between 1 and {max_amount}\n")
                continue
            # if inputted amount is valid it will return this amount. 
            return deposit
        except:
            print("Amount entered must a valid number\n") 
            continue


def get_lines():
    while True:
        user_input = input("\nPlease input a number of lines to bet on between 1 and 3: ")  

        try: 
            lines = int(user_input)

            if lines < 1 or lines > 3:
                print("\nLines entered must a number between 1 and 3")
                continue

            return lines
        except:
            print("\nLines entered must a valid number")
            continue

def main(): 
    # Assigning a return value of function "get_deposit" to variable called "deposit" 
    deposit = get_deposit()
    balance = deposit

    while True:    
        # Take input, convert to lowercase then assign it to variable called user_input
        user_input = input("\nPress Enter to play or Q to quit: ").lower()
        # if the user will input Q or q game will end
        if user_input == "q": 
            print("\nThank you for playing, see you again soon!")
            break

        print(f"\nYour balance is €{balance}")

        lines = get_lines()
        
main()