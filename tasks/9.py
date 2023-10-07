from res import Restaurant
from pirad import*
from collections import OrderedDict
from random import randint


def task1():
    '''
    Ресторан: создайте класс с именем Restaurant. Метод __init__() класса Restaurant должен содержать два атрибута: restaurant_name и cuisine_type. Создайте метод describe_
    restaurant(), который выводит два атрибута, и метод open_restaurant(), который выводит сообщение о том, что ресторан открыт.
    '''
    class Restaurant():
        def __init__(self, restaraunt_name, cuisine_type):
            """Инициализирует атрибуты restaurant_name и cuisine_type."""
            self.name = restaraunt_name
            self.type = cuisine_type
        
        def describe_restaraunt(self):
            '''Выводит два атрибута'''
            print(self.name.title(), self.type.title())
        
        def open_restaraunt(self):
            '''Вывоюдить сообщение об открытие ресторана'''
            print('Rrestaraunt is open!')  
    r = Restaurant("Aknurs method", "Nomad cuisine")
    r.describe_restaraunt()
    r.open_restaraunt()

def task2():
    '''
    Три ресторана: начните с класса из упражнения 9-1. Создайте три разных экземпляра, вызовите для каждого экземпляра метод describe_restaurant().
    '''
    class Restaurant():
        def __init__(self, restaraunt_name, cuisine_type):
            """Инициализирует атрибуты restaurant_name и cuisine_type."""
            self.name = restaraunt_name
            self.type = cuisine_type
        
        def describe_restaraunt(self):
            '''Выводит два атрибута'''
            print(self.name.title(), self.type.title())
        
        def open_restaraunt(self):
            '''Выводит сообщение об открытие ресторана'''
            print('Rrestaraunt is open!') 
    first = Restaurant("Aknurs method", "Nomad cuisine")
    second = Restaurant("Iem", "Eastern cuisine")
    third = Restaurant('Luna', 'Eastern and nomad cuisine')
    list = [first, second, third]
    for r in list:
        r.describe_restaraunt()
        r.open_restaraunt()

def task3():
    '''
    Пользователи: создайте класс с именем User. Создайте два атрибута first_name и last_name, а затем еще несколько атрибутов, которые обычно хранятся в профиле пользователя. 
    Напишите метод describe_user(), который выводит сводку с информацией о пользователе. Создайте еще один метод greet_user() для вывода персонального приветствия 
    для пользователя. Создайте несколько экземпляров, представляющих разных пользователей. Вызовите оба метода для каждого пользователя.
    '''
    class User():
        def __init__(self, first_name, last_name, age, gender):
            '''Инициализирует атрибуты'''
            self.fname = first_name
            self.lname = last_name
            self.age = age
            self.gender = gender 

        def describe_user(self):
            '''Выводит описание пользователя'''
            print(self.fname.title(), self.lname.title())
            print('\tAge:', self.age, '\tGender:', self.gender)

        def greet_user(self):
            '''Выводит сообщение с приветствием'''
            print('Hello,', self.fname.title())
    user = User('aknur', 'zhaxylykova', 18, 'woman')
    user1 = User('jimin', 'park', 26, 'men')
    user2 = User('taehyung', 'kim', 26, 'men')
    users = [user, user1, user2]
    for user in users:
        user.describe_user()
        user.greet_user()

def task4():
    '''
    Посетители: начните с программы из упражнения 9-1 (с. 165). Добавьте атрибут number_served со значением по умолчанию 0; он представляет количество обслуженных посетителей. 
    Создайте экземпляр с именем restaurant. Выведите значение number_served, потом измените и выведите снова. Добавьте метод с именем set_number_served(), 
    позволяющий задать количество обслуженных посетителей. Вызовите метод с новым числом, снова выведите значение.
    '''
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
    r = Restaurant('Aknurs method', 'Nomad cuisine')
    r.print_number()
    r.number_served = 12
    r.print_number()
    r.set_number_served(45)
    r.print_number()

def task5():
    '''
    Попытки входа: добавьте атрибут login_attempts в класс User из упражнения 9-3 (с. 165). Напишите метод increment_login_attempts(), увеличивающий значение login_
    attempts на 1. Напишите другой метод с именем reset_login_attempts(), обнуляющий значение login_attempts. Создайте экземпляр класса User 
    и вызовите increment_login_attempts() несколько раз. Выведите значение login_attempts, чтобы убедиться в том, что значение было изменено правильно, 
    а затем вызовите reset_login_attempts(). Снова выведите login_attempts и убедитесь в том, что значение обнулилось.
    '''
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
    user = User('aknur', 'zhaxylykova', 18, 'woman')
    user.increment_login_attempts()
    user.increment_login_attempts()
    user.read()
    user.reset_login_attempts()
    user.read()

def  task6():
    '''
    Киоск с мороженым: киоск с мороженым — особая разновидность ресторана. Напишите класс IceCreamStand, наследующий от класса Restaurant из упражнения 9-1 (с. 165) или
    упражнения 9-4 (с. 169). Подойдет любая версия класса; просто выберите ту, которая вам больше нравится. Добавьте атрибут с именем flavors для хранения списка сортов 
    мороженого. Напишите метод, который выводит этот список. Создайте экземпляр IceCreamStand и вызовите этот метод.
    '''
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
    IceCream = IceCrreamStand('Akurs method', 'Nomad')
    IceCream.print_flavors()

def task7():
    '''
    Администратор: администратор — особая разновидность пользователя. Напишите класс с именем Admin, наследующий от класса User из упражнения 9-3 (с. 165) или
    упражнения 9-5 (с. 170). Добавьте атрибут privileges для хранения списка строк вида «разрешено добавлять сообщения», «разрешено удалять пользователей», «разрешено
    банить пользователей» и т. д. Напишите метод show_privileges() для вывода набора привилегий администратора. Создайте экземпляр Admin и вызовите свой метод.
    '''
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

    class Admin(User):
        def __init__(self, first_name, last_name, age, gender):
            super().__init__(first_name, last_name, age, gender)
            self.privileges = ['разрешено добавлять сообщения', 'разрешено удалять пользователей', 'разрешено банить пользователей']
        
        def show_privilegas(self):
            '''Выводит привилегии админа'''
            print('Admin privilegas:')
            for p in self.privileges:
                print('\t', p)
    A = Admin('Aknur', 'Zhaxylykova', 18, 'woman')
    A.show_privilegas()

def task8():
    '''
    Привилегии: напишите класс Privileges. Класс должен содержать всего один атрибут privileges со списком строк из упражнения 9-7. Переместите метод show_privileges() в этот
    класс. Создайте экземпляр Privileges как атрибут класса Admin. Создайте новый экземпляр Admin и используйте свой метод для вывода списка привилегий.
    '''
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

    class Privilegas():
        def __init__(self, privilegas=['разрешено добавлять сообщения', 'разрешено удалять пользователей', 'разрешено банить пользователей']):
            self.privilegas = privilegas
        
        def show_privilegas(self):
            '''Выводит привилегии админа'''
            print('Admin privilegas:')
            for p in self.privilegas:
                print('\t', p)
          
    class Admin(User):
        def __init__(self, first_name, last_name, age, gender):
            super().__init__(first_name, last_name, age, gender)
            self.p = Privilegas()

    A = Admin('Aknur', 'Zhaxylykova', 18, 'woman')
    A.p.show_privilegas()

def task9():
    '''
    Обновление аккумулятора: используйте окончательную версию программы electric_car.py из этого раздела. Добавьте в класс Battery метод с именем upgrade_battery().
    Этот метод должен проверять размер аккумулятора и устанавливать мощность равной 85, если она имеет другое значение. Создайте экземпляр электромобиля с аккумулятором
    по умолчанию, вызовите get_range(), а затем вызовите get_range() во второй раз после вызова upgrade_battery(). Убедитесь в том, что запас хода увеличился.
    '''
    class Car():
        '''Простая модель автомобиля'''
        def __init__(self, make, model, year):
            self.make = make
            self.model = model
            self.year = year
            self.odometer_reading = 0

        def get_descriptive_name(self):
            long_name = str(self.year) + ' ' + self.make + ' ' + self.model
            return long_name.title()
        
        def read_odometer(self):
            print("This car has " + str(self.odometer_reading) + " miles on it.")
            
        def update_odometer(self, mileage):
            if mileage >= self.odometer_reading:
                self.odometer_reading = mileage
            else:
                print("You can't roll back an odometer!")

        def increment_odometer(self, miles):
            self.odometer_reading += miles 
    
    class Battery():
        """Простая модель аккумулятора электромобиля."""
        def __init__(self, battery_size=70):
            """Инициализирует атрибуты аккумулятора."""
            self.battery_size = battery_size
        
        def upgraid_battery(self):
            if self.battery_size != 85:
                self.battery_size = 85

        def describe_battery(self):
            """Выводит информацию о мощности аккумулятора."""
            print("This car has a " + str(self.battery_size) + "-kWh battery.") 

        def get_range(self):
            """Выводит приблизительный запас хода для аккумулятора."""
            if self.battery_size == 70:
                range = 240
            elif self.battery_size == 85:
                range = 270
            message = "This car can go approximately " + str(range)
            message += " miles on a full charge."
            print(message)

    class ElectricCar(Car):
        """Представляет аспекты машины, специфические для электромобилей."""
        def __init__(self, make, model, year):
            """
            Инициализирует атрибуты класса-родителя.
            Затем инициализирует атрибуты, специфические для электромобиля.
            """
            super().__init__(make, model, year)
            self.battery = Battery()
    my_tesla = ElectricCar('tesla', 'model s', 2016)
    my_tesla.battery.get_range()
    my_tesla.battery.upgraid_battery()
    my_tesla.battery.get_range()

def task10():
    '''
    Импортирование класса Restaurant: возьмите последнюю версию класса Restaurant и сохраните ее в модуле. Создайте отдельный файл, импортирующий класс Restaurant.
    Создайте экземпляр Restaurant и вызовите один из методов Restaurant, чтобы показать, что команда import работает правильно.
    '''
    r = Restaurant('Aknurs method', 'Nomad cuisine')
    r.print_number()

def task11():
    '''
    Импортирование класса Admin: начните с версии класса из упражнения 9-8 (с. 176). Сохраните классы User, Privileges и Admin в одном модуле. 
    Создайте отдельный файл, создайте экземпляр Admin и вызовите метод show_privileges(), чтобы показать, что все работает правильно.
    '''
    A = Admin('Aknur', 'Zhaxylykova', 18, 'woman')
    A.p.show_privilegas()

def task12():
    '''
    Множественные модули: сохраните класс User в одном модуле, а классы Privileges и Admin в другом модуле. В отдельном файле создайте экземпляр Admin и вызовите метод
    show_privileges(), чтобы показать, что все работает правильно.
    '''
    A = Admin('Aknur', 'Zhaxylykova', 18, 'woman')
    A.p.show_privilegas()

def task13():
    '''
    Переработка с OrderedDict Rewrite: начните с упражнения 6-4 (с. 113), в котором стандартный словарь используется для представления глоссария. Перепишите программу
    с использованием класса OrderedDict и убедитесь в том, что порядок вывода совпадает с порядком добавления пар «ключ—значение» в словарь.
    '''
    terms = OrderedDict()
    terms['range()'] = 'returns a sequence of numbers starting from zero and increment by 1 by default and stops before the given number'
    terms['sorted()'] = 'returns a sorted list from the items in an iterable'
    terms['sum()'] = 'the sum of all items in an iterable'
    terms['set()'] = ' used to convert any of the iterable to sequence of iterable elements with distinct elements'
    terms['append()'] = 'adds an item to the end of the list'
    for key, value in terms.items():
        print(key + ':', value, '\n')

def task14():
    '''
    Кубики: модуль random содержит функции для генерирования случайных чисел разными способами. Функция randint() возвращает целое число в заданном диапазоне. Следующий код 
    возвращает число от 1 до 6:
        from random import randint
        x = randint(1, 6)
    Создайте класс Die с одним атрибутом с именем sides, который содержит значение по умолчанию 6. Напишите метод roll_die() для вывода случайного числа от 1 до количества 
    сторон кубика. Создайте экземпляр, моделирующий 6-гранный кубик, и имитируйте 10 бросков. Создайте модели 10- и 20-гранного кубика. Имитируйте 10 бросков каждого кубика.
    '''
    class Die():
        def __init__(self, sides=6):
            self.sides = sides

        def roll_die(self):
            print('Тебе выпало', randint(1, self.sides), '!')
    d = Die()
    n = 10
    while n != 0:
        d.roll_die()
        n -= 1
    q = Die(10)
    n = 10
    while n != 0:
        q.roll_die()
        n -= 1

def task15():
    '''
    Модуль недели: для знакомства со стандартной библиотекой Python отлично подойдет сайт Python Module of the Week. Откройте сайт http://pymotw.com/ и просмотрите оглавление. 
    Найдите модуль, который покажется вам интересным, и прочитайте про него или изучите документацию по модулям collections и random.
    '''
    



