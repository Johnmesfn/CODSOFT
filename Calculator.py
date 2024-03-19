def display():
    print('********Welcome to terminal based Calculator********')
    print('This calculator performs some basic arithmetic functions listed below')
    print('Please press + for Addition \t     Please press - for Subtraction')
    print('Please press * for Multiplication \t Please press / for division')
    print('Please press ^ for exponentiation \t Please press % for modulo')
    print('               Please press any key to terminate ')


# The addition operator works when the user enter a number but as soon as the user enters '='
# The addition operation halts and displays the result
def addition():
    sum = 0
    print("This addition works like a calculator when the user enters '=' sign it gives results but")
    try:
        number_1 = input('Enter a number: ')
        counter = 0
        while number_1.isnumeric():
            sum = sum + float(number_1)
            counter = counter + 1
            number_1 = input('Enter a number: ')
        while counter < 2:
            print('To operate this operation you need at least two numbers ')
            number_1 = input('Enter a number: ')
            while number_1.isnumeric():
                sum = sum + float(number_1)
                counter = counter + 1
                number_1 = input('Enter a number: ')
    except Exception as e:
        print(e)
    return sum


def subtraction(): # 12 3 4 98
    difference = 0
    print("This subtraction works like a calculator when the user enters '=' sign it gives results but")
    try:
        number_1 = input('Enter a number: ')
        counter = 0
        if number_1.isnumeric():
            difference = float(number_1)
            number_1 = input('Enter a number: ')
            counter = counter + 1
            while number_1.isnumeric():
                difference = difference - float(number_1)
                number_1 = input('Enter a number: ')
                counter = counter + 1
        while counter < 2:
            print('To operate this operation you need at least two numbers ')
            number_1 = input('Enter a number: ')
            if number_1.isnumeric():
                difference = number_1
                number_1 = input('Enter a number: ')
                while number_1.isnumeric():
                    difference = difference - float(number_1)
                    number_1 = input('Enter a number: ')
    except Exception as e:
        print(e)
    return difference


def multiplication():
    product = 1
    print("This Multiplication works like a calculator when the user enters '=' sign it gives results but")
    try:
        number_1 = input('Enter a number: ')
        counter = 0
        while number_1.isnumeric():
            product = product * float(number_1)
            counter = counter + 1
            number_1 = input('Enter a number: ')
        while counter < 2:
            print('To operate this operation you need at least two numbers ')
            number_1 = input('Enter a number: ')
            while number_1.isnumeric():
                product = product * float(number_1)
                counter = counter + 1
                number_1 = input('Enter a number: ')
    except Exception as e:
        print(e)
    return product


def division():
    quotient = 0
    try:
        number_1 = float(input('Enter the dividend: '))
        number_2 = float(input('Enter the divisor: '))
        quotient = number_1 / number_2
    except Exception as e:
        print(e)
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
