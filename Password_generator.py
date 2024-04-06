import random
def password_generator(length):
    print('Please Select from the list of menus below') 
    print('Press 1 for aLpahbeT password')
    print('Press 2 for Numerical password')
    print('Press 3 for Special character password')
    print(' Press 4 for alphanumerical password')
    print('Press 5 for alphanumerical and special character password')
    password_desire = input()
    while password_desire != '1' and password_desire != '2' and password_desire != '3' and password_desire != '4' and password_desire != '5':
        print('Please enter a valid input')
        print('Please Select from the list of menus below') 
        print('Press 1 for aLpahbeT password \t')
        print('Press 2 for Numerical password \t')
        print('Press 3 for Special character password \t')
        print('Press 4 for alphanumerical password \t')
        print('Press 5 for alphanumerical and special character password \t')
        password_desire = input()
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

    upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

    special_characters = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                          '*', '(', ')', '<', '[', ']', '{', '}', '!', ';', '&']
    if password_desire == '1':
        password_characters = small_letters + upper_letters
        random_password = ''.join(random.choice(password_characters) for i in range(length))
        return random_password
    elif password_desire == '2':
        password_characters = numbers
        random_password = ''.join(random.choice(password_characters) for i in range(length))
        return random_password
    elif password_desire == '3':
        password_characters = special_characters
        random_password = ''.join(random.choice(password_characters) for i in range(length))
        return random_password
    elif password_desire == '4':
        password_characters = small_letters + upper_letters + numbers
        random_password = ''.join(random.choice(password_characters) for i in range(length))
        return random_password
    elif password_desire == '5':
        password_characters = small_letters + upper_letters + numbers + special_characters
        random_password = ''.join(random.choice(password_characters) for i in range(length))
        return random_password 

def length_input():
    length = input('Please enter the desired length ').strip()
    while not length.isnumeric():
        print('Sorry password length must be a number')
        length = input('Please enter the desired length ').strip()
    while int(length) <= 0:
        print("Password length can't be less than 1")
        length = input('Please enter the desired length ').strip()
    return int(length)

def main():
    print('********** Welcome to terminal based password generator **********')
    length = length_input()
    generated_password = password_generator(length)
    if length <= 8:
        print('We consider your password is Weak based on its length we recommend a length greater than 8')
        print(f'The generated password is: {generated_password}')
        choice = input('Press 1 to generate again press any key to terminate: ').strip()
        if choice == '1':
            main()
        else:
            print('Thank you for using the service')
            exit()
    else:
        print('We consider your password is Strong')
        print(f'The generated password is: {generated_password}')
        choice = input('Press 1 to generate again press any key to terminate: ').strip()
        if choice == '1':
            main()
        else:
            print('Thank you for using the service')
            exit()
if __name__ == "__main__":
    main()
