class Restaurant():
        def __init__(self, restaraunt_name, cuisine_type):
            """Инициализирует атрибуты restaurant_name и cuisine_type."""
            self.name = restaraunt_name
            self.type = cuisine_type
            self.number_served = 0
        
        def describe_restaraunt(self):
            '''Выводит два атрибута'''
            print(self.name.title(), self.type.title())
        
        def open_restaraunt(self):
            '''Вывоюдить сообщение об открытие ресторана'''
            print('Rrestaraunt is open!')

        def print_number(self):
            '''Выводит кол-во посетителей'''
            print('Number served =', self.number_served)

        def set_number_served(self, number):
            '''Задает кол-во посетителей'''
            self.number_served = number
    
class IceCrreamStand(Restaurant):
    def __init__(self, restaraunt_name, cuisine_type):
        super().__init__(restaraunt_name, cuisine_type)
        self.flavors = ['Vanilla', 'Cookieas and cream', 'Butter pecan']
        
    def print_flavors(self):
        '''Выводит сорты мороженого'''
        print('Ice cream varieties:')
        for f in self.flavors:
            print('\t', f)

class User():
    def __init__(self, first_name, last_name, age, gender):
        '''Инициализирует атрибуты'''
        self.fname = first_name
        self.lname = last_name
        self.age = age
        self.gender = gender 
        self.login_attempts = 0

    def increment_login_attempts(self):
        '''Увеличивает значение login_attempts'''
        self.login_attempts += 1

    def reset_login_attempts(self):
        '''Обнуляет значение login_attempts'''
        self.login_attempts = 0 

    def read(self):
        '''Выводит значение login_attempts'''
        print(self.login_attempts)
    def describe_user(self):
        '''Выводит описание пользователя'''
        print(self.fname.title(), self.lname.title())
        print('\tAge:', self.age, '\tGender:', self.gender)

    def greet_user(self):
        '''Выводит сообщение с приветствием'''
        print('Hello,', self.fname.title())
