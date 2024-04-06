def display():
    print('********Welcome to terminal based Calculator********')
    print('This calculator performs some basic arithmetic functions listed below')
    print('Please press + for Addition \t     Please press - for Subtraction')
    print('Please press * for Multiplication \t Please press / for Long Division')
    print('Please press ^ for Exponentiation \n')
    print('               Please press any key to terminate ')
# The addition operator works initialy asking the quantities of numbers they want to add.
# And asks them to enter the numbers  
# The addition operation halts and displays the result
# Function to add numbers
def addition():
    sum = 0  # Initialize sum
    print ('How many number would like to add: ') # Ask user how many numbers they want to add
    number_of_numbers = input() # Get input from user
    while not number_of_numbers.isnumeric():
        print('Please enter a valid number')  # Print error message
        number_of_numbers = input()  # Get new input from user
    number_of_numbers = int(number_of_numbers) # Convert input to integer
    for i in range(number_of_numbers):  # Loop for number of numbers
        number = input('Enter a number: ')  # Get input from user
        while not number.isnumeric():  # Check if input is numeric
            print('Please enter a valid number')  # Print error message
            number = input('Enter a number: ')  # Get new input from user
        print('Is number positive? Y for Yes or N for No')  # Ask user if number is Positive 
        sign = input()  # Get input from user
        while sign.upper() != 'Y' and sign.upper() != 'N':  # Check if user's choice is valid
            print('Invalid choice selected.')  # Print error message
            print('Is number positive? Y for Yes or N for No')  # Ask user if number is Positive
            sign = input()  # Get input from user again
        if sign.upper() == 'Y':  # Check if user's choice is positive
            number = float(number)  # Convert input to float
        elif sign.upper() == 'N':  # Check if user's choice is negative
            number = -1 * float(number)  # Make the number negative
        sum = sum + float(number)  # Add number to sum
    return sum  # Return sum so it can be used in other operations

# Function to subtract numbers
def subtraction():
    difference = 0  # Initialize difference
    number = [] 
    number_of_numbers = input('How many number would like to subtract: ')  # Ask user how many numbers they want to multiply
    while not number_of_numbers.isnumeric():  # Check if input is numeric
        print("Number of arguments expected, please enter a valid number")  # Print error message
        number_of_numbers = input()  # Get new input from user
    number_of_numbers = int(number_of_numbers)  # Convert input to integer
    for i in range(number_of_numbers):  # Loop for number of numbers
        num = input("Enter a number: ")  # Get input from user
        while not num.isnumeric():  # Check if input is numeric
            print("Please enter a valid number")  # Print error message
            num = input("Enter a number: ")  # Get new input from user
        print("Is number positive? Y for Yes or N for No")  # Ask user if number is Positive
        sign = input()  # Get input from user
        while sign.upper() != 'Y' and sign.upper() != 'N':  # Check if user's choice is valid
            print("Invalid choice selected.")  # Print error message
            print("Is number positive? Y for Yes or N for No")  # Ask user if number is Positive
            sign = input()  # Get input from user again
        if sign.upper() == 'Y':  # Check if user's choice is positive
            num = float(num)  # Convert input to float
        elif sign.upper() == 'N':  # Check if user's choice is negative
            num = -1 * float(num)  # Make the number negative
        number.append(float(num))  # Add number to list
    difference = number[0] - sum(number[1:])  # Subtract numbers from list starting with first element
    return difference  # Return difference so it can be used in other operations

# This function calculates the product of multiple numbers.
# It takes an arbitrary number of numbers as input and returns the product.
def multiplication():
    product = 1  # Initialize difference
    number_of_numbers = input('How many number would like to multiply: ')  # Ask user how many numbers they want to multiply
    while not number_of_numbers.isnumeric():  # Check if input is numeric
        print("Number of arguments expected, please enter a valid number")  # Print error message
        number_of_numbers = input()  # Get new input from user
    number_of_numbers = int(number_of_numbers)  # Convert input to integer
    for i in range(number_of_numbers):  # Loop for number of numbers
        number = input('Enter a number: ')  # Get input from user
        while not number.isnumeric():  # Check if input is numeric
            print('Please enter a valid number')  # Print error message
            number = input('Enter a number: ')  # Get new input from user
        print('Is number positive? Y for Yes or N for No')  # Ask user if number is Positive 
        sign = input()  # Get input from user
        while sign.upper() != 'Y' and sign.upper() != 'N':  # Check if user's choice is valid
            print('Invalid choice selected.')  # Print error message
            print('Is number positive? Y for Yes or N for No')  # Ask user if number is Positive
            sign = input()  # Get input from user again
        if sign.upper() == 'Y':  # Check if user's choice is positive
            number = float(number)  # Convert input to float
        elif sign.upper() == 'N':  # Check if user's choice is negative
            number = -1 * float(number)  # Make the number negative
        product = product * float(number)  # Multiply number with product
    return product  # Return product so it can be used in other operations

# This function performs long division by calculating the  quotient and remainder.
# The division is performed using Euclidean algorithm.
# It takes two numbers, dividend and divisor, and returns the quotient and remainder.
def division_long(dividend, divisor):
    quotient = 0 # Initialize quotient to zero
    remainder = dividend # Initialize remainder to dividend
    while float(remainder) >= float(divisor): # Loop until remainder is less than divisor
        remainder -= divisor # Subtract divisor from remainder
        quotient += 1 # Add one to quotient
    return quotient, remainder # Return quotient and remainder

# Main program that handles user inputs for division operation.
def division():
    quotient = 0 # Initialize quotient to zero
    remainder = 0 # Initialize remainder to zero
    dividend = input('Enter the dividend: ') # Get dividend from user input
    while not dividend.isnumeric(): # Check if input is numeric
        print('Please enter a valid number') # Print error message
        dividend = input('Enter the dividend: ') # Get new input from user
    dividend = float(dividend) # Convert input to float
    divisor = input('Enter the divisor: ') # Get divisor from user input
    while not divisor.isnumeric(): # Check if input is numeric
        print('Please enter a valid number') # Print error message
        divisor = input('Enter the divisor: ') # Get new input from user
    while divisor == '0': # Check if input is numeric and divisor is zero
        print("Error! Division by zero is not possible") # Print error message
        divisor = input('Enter the divisor: ') # Get new input from user 
        while not divisor.isnumeric(): # Check if input is numeric
            print('Please enter a valid number') # Print error message
            divisor = input('Enter the divisor: ') # Get new input from user       
    divisor = float(divisor) # Convert input to float
    try: # Try to convert input to float and perform division
        quotient, remainder = division_long(dividend, divisor) # Calculate quotient and remainder
    except Exception as e: # Catch errors caused by non-numeric input
        print(f'Error! {e}') # Print error message
    return quotient, remainder # Return quotient and remainder
def power():
    exponentiation = 0 # Initialize exponentiation to zero
    base = input("Enter the base: ") # Get base from user input
    while not base .isnumeric(): # Check if input is numeric
        print('Please enter a valid base') # Print error message
        base = input("Enter the base: ") # Get new input from user
    print('Is the base Positive? Y for Yes or N for No') # Ask user if base is negative
    choice = input()     # Get user's choice
    while choice.upper() != 'Y' and choice.upper() != 'N':  # Check if user's choice is valid
        print('Invalid choice selected.') # Print error message
        print('Is the base Positive? Y for Yes or N for No') # Ask user if base is negative
        choice = input() # Get user's choice
    if choice.upper() == 'Y': # Check if user's choice is positive
        power = input("Enter the exponent: ") # Get exponent from user input
        while not power.isnumeric(): # Check if input is numeric
            print('Please enter a valid exponent')  # Print error message
            power = input("Enter the exponent: ") # Get new input from user
        print('Is the exponet Positive? Y for Yes or N for No') # Ask user if base is negative
        choice = input()     # Get user's choice
        while choice.upper() != 'Y' and choice.upper() != 'N':  # Check if user's choice is valid
            print('Invalid choice selected.') # Print error message
            print('Is the exponet Positive? Y for Yes or N for No') # Ask user if base is negative
            choice = input() # Get user's choice
        if choice.upper() == 'Y': # Check if user's choice is positive
            exponentiation = int(base) ** int(power) # Calculate exponentiation
        elif choice.lower() == "n": # Check if user's choice is negative
            power = -1 * int(power) # Making the power negativ
            exponentiation = pow(int(base), int(power)) # Calculate exponentiation with negative power 
    else: # Base is negative 
        base = -1 * int(base) # Making the base negative
        power = input("Enter the exponent: ") # Get exponent from user input
        while not power.isnumeric(): # Check if input is numeric
            print('Please enter a valid exponent')  # Print error message
            power = input("Enter the exponent: ") # Get new input from user
        print('Is the exponet Positive? Y for Yes or N for No') # Ask user if exponent is Positive
        choice = input()     # Get user's choice
        while choice.upper() != 'Y' and choice.upper() != 'N':  # Check if user's choice is valid
            print('Invalid choice selected.') # Print error message
            print('Is the exponet Positive? Y for Yes or N for No') # Ask user if base is negative
            choice = input() # Get user's choice
        if choice.upper() == 'Y': # Check if user's choice is positive
            exponentiation = int(base) ** int(power) # Calculate exponentiation
        elif choice.lower() == "n": # Check if user's choice is negative, then take absolute value of both base and exponent without taking into account that base is negative
            power = -1 * int(power) # Making the power negative
            exponentiation = pow(int(base), int(power)) # Calculate exponentiation with negative power 
    return exponentiation # Return result of exponentiation

def main():
    display()
    choice = input(' ')
    while choice == '+' or choice == '-' or choice == '*' or choice == '/' or choice == '^' or choice == '%':
        if choice == '+':
            sum = addition()
            print(f'Your sum is: {sum}')
            main()
        elif choice == '-':
            difference = subtraction()
            print(f'Your difference is: {difference}')
            main()
        elif choice == '*':
            print('Your product is: ', multiplication())
            main()
        elif choice == '/':
            quotient , remainder = division()
            print(f'Your quotient is: {quotient} and your remainder is: {remainder}')
            main()
        elif choice == '^':
            exponentiation = power()
            print(f'Your exponential is: {exponentiation}')
            main()
    print('Are you sure to terminate the program? Y for Yes or N for No')
    choice = input()
    while choice.upper() != 'Y' and choice.upper() != 'N':
        print('Invalid choice selected.')
        print('Are you sure to terminate the program? Y for Yes or N for No')
        choice = input()
    if choice.upper() == 'Y':
        exit()
    elif choice.upper() == 'N':
        main()


if __name__ == "__main__":
    main()
