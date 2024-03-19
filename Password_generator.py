import random


def password_generator(length):
    while length <= 0:
        print('Password length must be greater than 0. ')
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
    password_characters = numbers + small_letters + upper_letters + special_characters
    random_password = ''.join(random.choice(password_characters) for i in range(length))
    return random_password


def length_input():
    print('********** Welcome to terminal based password generator **********')
    length = int(input('Please enter the desired length '))
    while length.isdigit() != 'False':
        print('Sorry password length must be a number')
        length = int(input('Please enter the desired length '))
    while length <= 0:
        print('Sorry password length must be greater than zero')
        length = int(input('Please enter the desired length '))
    return length


def main():
    length = length_input()
    generated_password = password_generator(length)
    if length <= 8:
        print('We consider your password is Weak based on its length we recommend a length greater than 8')
        print(f'The generated password is: {generated_password}')
        choice = input('Press 1 to generate again press any key to terminate: ')
        if choice == '1':
            main()
        else:
            print('Thank you for using the service')
            exit()
    else:
        print('We consider your password is Strong')
        print(f'The generated password is: {generated_password}')
        choice = input('Press 1 to generate again press any key to terminate: ')
        if choice == '1':
            main()
        else:
            print('Thank you for using the service')
            exit()


if __name__ == "__main__":
    main()
