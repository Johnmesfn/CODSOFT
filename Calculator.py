def display():
    print('********Welcome to terminal based Calculator********')
    print('This calculator performs some basic arithmetic functions listed below')
    print('Please press + for Addition \t     Please press - for Subtraction')
    print('Please press * for Multiplication \t Please press / for division')
    print('Please press ^ for exponentiation \t Please press % for modulo')
    print('               Please press any key to terminate ')


# The addition operator works when the user enter a number but as soon as the user enters '='
# The addition operation halts and displays the result
# Function to add numbers
def addition():
    sum = 0  # Initialize sum
    counter = 0  # Initialize counter
    # Get numbers and add them until 2 numbers are entered
    while counter < 2:
        try:
            number_1 = input('Enter a number: ')
            if not number_1.isnumeric():  # Check if input is non-numeric
                print('Please enter a valid number')
                continue
            sum = sum + float(number_1)  # Add number to sum
            counter = counter + 1  # Increment counter
        except Exception as e:  # Catch exceptions
            print(e)  # Print exception message
    return sum  # Return sum


# Function to subtract numbers
def subtraction():
    difference = 0  # Initialize difference
    print("This subtraction works like a calculator when the user enters '=' sign it gives results but")
    try:
        number_1 = input('Enter a number: ')
        counter = 0  # Initialize counter
        if number_1.isnumeric():  # Check if input is numeric
            difference = float(number_1)
            number_1 = input('Enter a number: ')
            counter = counter + 1  # Increment counter
            while number_1.isnumeric():  # Loop until non-numeric input
                difference = difference - float(number_1)
                number_1 = input('Enter a number: ')
    except Exception as e:  # Catch exceptions
        print(e)  # Print exception message
    return difference  # Return difference


# This function calculates the product of multiple numbers.
# It takes an arbitrary number of numbers as input and returns the product.
def multiplication():
    product = 1  # Initialize the product to 1
    print("This Multiplication works like a calculator when the user enters '=' sign it gives results but")
    try:
        number_1 = input('Enter a number: ')  # Request user input for the first number
        counter = 0  # Initialize the counter to 0

        # Validate and process the input until a non-numeric value is entered
        while number_1.isnumeric():
            product *= float(number_1)  # Multiply the product by the input number
            counter += 1  # Increment the counter
            number_1 = input('Enter a number: ')  # Request user input for the next number

        # Ensure that at least two numbers are entered
        while counter < 2:
            print('To operate this operation you need at least two numbers ')  # Inform the user about the requirement
            number_1 = input('Enter a number: ')  # Request user input for the next number

            # Validate and process the input until a non-numeric value is entered
            while number_1.isnumeric():
                product *= float(number_1)  # Multiply the product by the input number
                counter += 1  # Increment the counter
                number_1 = input('Enter a number: ')  # Request user input for the next number
    except Exception as e:
        print(e)  # Print exception message
    else:
        return product  # Return the product


# This function performs division of two numbers
def division():
    # Initialize the quotient to 0
    quotient = 0
    # Get the dividend from user input and convert it to a float
            number_1 = float(input('Enter the dividend: '))
            # Get the divisor from user input and convert it to a float
            number_2 = float(input('Enter the divisor: ')
            # Perform division of number_1 by number_2
            quotient = number_1 / number_2
            # Capture any exceptions that occur during the execution of the code
    try:  
    # Get the dividend from user input and convert it to a float , then check if it's zero
        number_1 = float(input('Enter the dividend: '))
        # Get the divisor from user input and convert it to a float
        number_2 = float(input('Enter the divisor: ')
        # Perform division of number_1 by number_2
        quotient = number_1 / number_2
        # Capture any exceptions that occur during the execution of the code
    except Exception as e:
        # Print the exception message
        print(e)
    # Return the quotient
    return quotient


def exponentiation():
    exponentiation = 0
    try:
        number_1 = float(input('Enter the base: '))
        number_2 = float(input('Enter the exponent: '))
        exponentiation = number_1 ** number_2
    except Exception as e:
        print(e)
    return exponentiation


def modulo():
    remainder = 0
    try:
        number_1 = float(input('Enter the dividend: '))
        number_2 = float(input('Enter the divisor: '))
        remainder = number_1 % number_2
    except Exception as e:
        print(e)
    return remainder


def main():
    display()
    choice = input(' ')
    while choice == '+' or choice == '-' or choice == '*' or choice == '/' or choice == '^' or choice == '%':
        if choice == '+':
            print('Your sum is: ', addition())
            main()
        elif choice == '-':
            print('Your difference is: ', subtraction())
            main()
        elif choice == '*':
            print('Your product is: ', multiplication())
            main()
        elif choice == '/':
            print('Your quotient is: ', division())
            main()
        elif choice == '^':
            print('Your exponential is: ', exponentiation())
            main()
        elif choice == '%':
            print('Your remainder is: ', modulo())
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
