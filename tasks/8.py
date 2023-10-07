#8.16
from print_model import*
from print_model import print_models
from print_model import show_completed_models as shh


#8.15
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
shh(completed_models)


#8.1
#Сообщение: напишите функцию display_message() для вывода сообщения по теме, рассматриваемой в этой главе. 
# Вызовите функцию и убедитесь в том, что сообщение выводится правильно.
def display_message():
    '''Выводить сообщение с информацией из 8-ой главы'''
    print('Эта глава посвящена функциям — именованным блокам кода, предназначенным для решения одной конкретной задачи. Чтобы выполнить задачу, определенную в виде функции, вы указываете имя функции, отвечающей за эту задачу. Если задача должна многократно выполняться в программе, вам не придется заново вводить весь необходимый код; просто вызовите функцию, предназначенную для решения задачи, и этот вызов приказывает Python выполнить код, содержащийся внутри функции. Как вы вскоре убедитесь, использование функций упрощает чтение, написание, тестирование кода и исправление ошибок. В этой главе также рассматриваются возможности передачи информации функциям. Вы узнаете, как писать функции, основной задачей которых является вывод информации, и другие функции, предназначенные для обработки данных и возвращения значения (или набора значений.) Наконец, вы научитесь хранить функции в отдельных файлах, называемых модулями, для упорядочения файлов основной программы.')
display_message()

#8.2
#Любимая книга: напишите функцию favorite_book(), которая получает один параметр title. Функция должна выводить сообщение вида 
# «One of my favorite books is Alice in Wonderland». Вызовите функцию и убедитесь в том, что название книги правильно передается как аргумент при вызове функйии.
def favorite_book(title):
    '''Выводить сообщение о любимой книге'''
    print('\nOne of my favorite book is', title.title())
favorite_book('the little prince')

#8.3
#Футболка: напишите функцию make_shirt(), которая получает размер футболки и текст, который должен быть напечатан на ней. Функция должна выводить сообщение с размером
#и текстом. Вызовите функцию с использованием позиционных аргументов. Вызовите функцию во второй раз с использованием именованных аргументов.
def make_shirt(size, text):
    '''Выводить сообщение о размере и принте футболки'''
    print('\nSize:', size, '\nPrint:', text)
make_shirt(42, 'Call me by your name')
make_shirt(text = 'Call me by your name', size = 42)

#8.4
# Большие футболки: измените функцию make_shirt(), чтобы футболки по умолчанию имели размер L, и на них выводился текст «I love Python.». Создайте футболку с размером
#L и текстом по умолчанию, а также футболку любого размера с другим текстом.
def make_shirt(text = 'I love python', size = 'L'):
    '''Выводить сообщение о размере и принте футболки'''
    print('\nSize:', size, '\nPrint:', text)
make_shirt()
make_shirt(text = 'Call me by your name', size = 'S')

#8.5
# Города: напишите функцию describe_city(), которая получает названия города и страны. Функция должна выводить простое сообщение (например, «Reykjavik is in Iceland»). 
# Задайте параметру страны значение по умолчанию. Вызовите свою функцию для трех  разных городов, по крайней мере один из которых не находится в стране по умолчанию.
def describe_city(city, country = 'Kazakhstan'):
    '''Выводить сообщение с названием города и его страны'''
    print('\n', city.title(), 'is in', country.title())
describe_city('nur-sultan')
describe_city(city = 'almaty')
describe_city('berlin', 'Germany')

#8.6
# Названия городов: напишите функцию city_country(), которая получает название города и страну. Функция должна возвращать строку в формате “Santiago, Chile”. 
# Вызовите свою функцию по крайней мере для трех пар «город—страна» и выведите возвращенное значение.
def city_country(city, country):
    '''Возвращает отформатированные названия страны и города '''
    country_city = country + ', ' + city
    return country_city.title()
print(city_country('berlin', 'germany'))

#8.7
#Альбом: напишите функцию make_album(), которая строит словарь с описанием музыкального альбома. Функция должна получать имя исполнителя и название альбома
#и возвращать словарь, содержащий эти два вида информации. Используйте функцию
#для создания трех словарей, представляющих разные альбомы. Выведите все возвращаемые значения, чтобы показать, что информация правильно сохраняется во всех трех
#словарях.
#Добавьте в make_album() дополнительный параметр для сохранения количества дорожек в альбоме. Если в строку вызова включено значение количества дорожек, 
# добавьте это значение в словарь альбома. Создайте как минимум один новый вызов функции с передачей количества дорожек в альбоме.
def make_album(performer, name, number=''):
    '''Возвращает словарь с информацией об альбоме'''
    album = {'performer': performer, 'name': name}
    if number:
        album['number'] = number
    return album
print(make_album('BTS', 'BE'))
print(make_album('Ariana Grande', 'Sweetener'))
print(make_album('Moldanazae', 'Aitarym kop', 6))

#8.8
#. Пользовательские альбомы: начните с программы из упражнения 8-7. Напишите цикл while, в котором пользователь вводит исполнителя и название альбома. 
# Затем в цикле вызывается функция make_album() для введенных пользователей и выводится созданный словарь. Не забудьте предусмотреть признак завершения в цикле while.
def make_album(performer, name, number=''):
    '''Возвращает словарь с информацией об альбоме'''
    album = {'performer': performer, 'name': name}
    if number:
        album['number'] = number
    return album
while True:
    print('\nPlease enter album details.')
    print("(enter 'q' at any time to quit)")
    p = input('Album performer:')
    if p == 'q':
        break
    n = input('Album name:')
    if n == 'q':
        break
    nu = input('Number (is not necessary):')
    if nu == 'q':
        break
    print(make_album(p, n, nu))

#8.9
#Фокусники: создайте список с именами фокусников. Передайте список функции show_magicians(), которая выводит имя каждого фокусника в списке.
def show_magiciance(magiciance):
    '''Выводить имена фокусников'''
    for m in magiciance:
        print(m.title())
magic = ['qwe', 'rty', 'yui']
show_magiciance(magic)

#8.10
#Великие фокусники: начните с копии вашей программы из упражнения 8-9. Напишите функцию make_great(), которая изменяет список фокусников, добавляя к имени каждого
#фокусника приставку «Great». Вызовите функцию show_magicians() и убедитесь в том, что список был успешно изменен.
def make_great(magic, great):
    '''Изменяет список имен'''
    for names in magic:
        great_name = 'Great' + names
        great.append(great_name)

def show_magiciance(great):
    '''Выводить имена фокусников'''
    for great_names in great:
        print(great_names.title())
magic = ['qwe', 'rty', 'uio']
great = []
make_great(magic, great)
show_magiciance(great)

#8.11
#Фокусники без изменений: начните с программы из упражнения 8-10. Вызовите функцию make_great() и передайте ей копию списка имен фокусников. Поскольку исходный
#список остался неизменным, верните новый список и сохраните его в отдельном списке.
#Вызовите функцию show_magicians() с каждым списком, чтобы показать, что в одном списке остались исходные имена, а в другом к имени каждого фокусника добавилась приставка
#«Great».
def make_great(magic, great):
    '''Изменяет список имен'''
    for names in magic:
        great_name = 'Great' + names
        great.append(great_name)

def show_magiciance(great):
    '''Выводить имена фокусников'''
    for great_names in great:
        print(great_names.title())
magic = ['qwe', 'rty', 'uio']
great = []
make_great(magic[:], great)
show_magiciance(great)
show_magiciance(magic)

#8.12
#Сэндвичи: напишите функцию, которая получает список компонентов сэндвича. Функция должна иметь один параметр для любого количества значений, переданных при вызове
#функции, и выводить описание заказанного сэндвича. Вызовите функцию три раза с разными количествами аргументов.
def sandwich(*components):
    '''Выводить список компонентов сэндвича'''
    print('Sandwich componets:')
    for component in components:
        print('\t-', component)
sandwich('qwe', 'rty', 'iop')
sandwich('lkjh', 'asd')
sandwich('polknvghsv')

#8.13
#. Профиль: начните с копии программы user_profile.py. Создайте собственный профиль вызовом build_profile(), укажите имя, фамилию и три другие пары «ключ—значение» 
# для вашего описания.
def build_profile(first, last, **user_info):
    '''Сохраняет профиль'''
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    print(profile)
build_profile('Aknur', 'Zhaxylykova', age=18,
               gender='woman', favorite_color='blue')

#8.14
# Автомобили: напишите функцию для сохранения информации об автомобиле в словаре. Функция всегда должна возвращать производителя и название модели, но при этом она
#может получать произвольное количество именованных аргументов. Вызовите функцию с передачей обязательной информации и еще двух пар «имя—значение» (например, цвет и комплектация).
#  Ваша функция должна работать для вызовов следующего вида:
            #car = make_car(‘subaru’, ‘outback’, color=’blue’, tow_package=True)
#Выведите возвращаемый словарь и убедитесь в том, что вся информация была сохранена правильно.
def make_car(name, producer, **car_info):
    '''Сохраняет информацию о машине'''
    car = {}
    car['car name'] = name
    car['car producer'] = producer
    for key, value in car_info.items():
        car[key] = value
    print(car)
make_car('subaru', 'outback', color='blue', tow_package=True)

















