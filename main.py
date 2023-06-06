def get_deposit():
    while True:
        user_input = input("Please input deposit amount between 1 and 1000: ")
        # Trys to convert user_input to integer
        try: 
            deposit = int(user_input)
            # Checks if deposit amount is less than or equal to 0 or greater than 1000
            # If the amount is less than equal to 0 or greater than 1000 it will loop back to the beginning and ask the user to input a valid amount
            if deposit <= 0 or deposit > 1000: 
                print("Amount must be a number between 1 and 1000\n")
                continue
            # if inputted amount is valid it will return this amount. 
            return deposit
        except:
            print("Amount entered must a valid number\n") 
            continue

    
def main(): 
    # Assigning a return value of function "get_deposit" to variable called "deposit" 
    deposit = get_deposit()

main()