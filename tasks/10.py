def task_10_1():
    with open('learning_python.txt') as file_object:
        content = file_object.read()
        print(content.rstrip())

    with open('learning_python.txt') as file_object:
        for line in file_object:
            print(line)
        
    with open('learning_python.txt') as file_object:
        lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())

def task_10_2():
    with open('learning_python.txt') as file_object:
        content = file_object.read()
        content = content.replace('python', 'c++')
        print(content)

def task_10_3():
    with open('guest.txt', 'w') as file_object:
        guest_name = input('Enter your name:')  
        file_object.write(guest_name + '\n') 

def task_10_4():
    with open('guest.txt', 'a') as file_object:
        while True:
            guest_name = input('Enter your name (enter "q" for stop):')
            if guest_name == 'q':
                break
            else:
                file_object.write(guest_name + '\n')

def task_10_5():
    with open('interview.txt', 'a') as file_object:
        while True:
            interviews = input('Why do you like Python? (enter "q" for stop):')
            if interviews == 'q':
                break
            else:
                file_object.write(interviews + '\n')

def task_10_6():
    first_number = input("\nFirst number: ")
    second_number = input("Second number: ")
    try: 
        answer = int(first_number) - int(second_number)    
    except ValueError:        
        print("Enter NUMBER!!!!!")    
    else: print(answer)

def task_10_7():
    print("Give me two numbers, and I'll MINUS them.") 
    print("Enter 'q' to quit.")
    while True: 
        first_number = input("\nFirst number: ") 
        if first_number == 'q':
            break 
        second_number = input("Second number: ")
        if second_number == 'q':
            break     
        try: 
            answer = int(first_number) - int(second_number)    
        except ValueError:        
            print("Enter NUMBER!!!!!")    
        else: print(answer)

def task_10_8():
    try:
        with open('cats.txt') as cats, open('dogs.txt') as dogs:
            Cats = cats.read()
            print(Cats.rstrip())
            Dogs = dogs.read()
            print(Dogs.rstrip())
    except FileNotFoundError:
        print("This file doesn't exist")

def task_10_9():
    files = ['cats.txt', 'dogs.txt', 'hamsters.txt']
    def output(filename):
        try:
            with open(filename) as file_object:
                content = file_object.read()
                print(content.rstrip())
        except FileNotFoundError:
            pass
    for file in files:
        output(file)

def task_10_10():
    books = ['first_book.txt', 'second_book.txt']#, 'third_book.txt']
    for book in books:
        with open(book) as file_object:
            content = file_object.read()
            print(content.count('the'), content.lower().count('the'))

    with open('third_book.txt', encoding='utf-8', newline='') as third:
        content = third.read()
        print(content.count('the'), content.lower().count('the'))


import json


def task_10_11():
    number = input('Enter your favorite number:')
    filename = 'number.json'
    
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
        print("Great, we'll memorize it!\n")
    
    with open(filename) as f_obj:
        number = json.load(f_obj)
        print("I know your favorite number! It's " + number)

def task_10_12():
    filename = 'number.json'
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        number = input('Enter your favorite number:')
        with open(filename, 'w') as f_obj:
            json.dump(number, f_obj)
            print("Great, we'll memorize it!")
    else:
        print("I know your favorite number! It's " + number)

def task_10_13():
    def get_stored_username():
        '''Получает хранимое имя пользователя'''
        filename = 'username.json'
        try:
            with open(filename) as f_obj:
                username = json.load(f_obj)
        except FileNotFoundError:
            return None
        else:
            return username
    
    def get_new_username():
        '''Запрашивает новое имя пользователя'''
        username = input('What is your name?')
        filename = 'username.json'
        with open(filename, 'w') as f_obj:
                json.dump(username, f_obj)
                return username

    def greet_user():
        '''Приветсвует пользователя по имени'''
        username = get_stored_username()
        if username:
            correct_name = input('Your name '+username+'\nIs it correct?')
            if correct_name == 'Yes':
                print('Welcome back, ' + username + '!')
            else:
                username = get_new_username()
                print("We'll remember you when you come back, " + username)
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username)
    greet_user()
task_10_10()