#7.1
#Прокат машин: напишите программу, которая спрашивает у пользователя, какую машину он хотел бы взять напрокат.
# Выведите сообщение с введенными данными (например, “Let me see if I can find you a Subaru”).
car_name = input('Let me see if I can find you a ')

#7.2
#Заказ стола: напишите программу, которая спрашивает у пользователя, на сколько
#мест он хочет забронировать стол в ресторане. Если введенное число больше 8, выведите
#сообщение о том, что пользователю придется подождать. В противном случае сообщите, что стол готов.
tables = int(input('Сізге қанша үстел қажет? '))
if tables <= 8:
    print('Тапсырыс дайын.')
else:
    print('Күтуге тура келеді.')

#7.3
#Числа, кратные 10: запросите у пользователя число и сообщите, кратно оно 10 или нет.
number = int(input('Өтініш сан таңдаңыз.'))
if number % 10 == 0:
    print(True)
else:
    print(False)

#7.4
#Дополнения для пиццы: напишите цикл, который предлагает пользователю вводить дополнения для пиццы до тех пор, 
# пока не будет введено значение 'quit’. При вводе каждого дополнения выведите сообщение о том, что это дополнение включено в заказ.
while True:
    topping = input('Please select the topping.')
    if topping == 'quite':
        break
    else:
        print(topping.title() + ' ' + 'was added.')

#7.5
#Билеты в кино: кинотеатр установил несколько вариантов цены на билеты в зависимости от возраста посетителя. 
# Для посетителей младше 3 лет билет бесплатный; в возрасте от 3 до 12 билет стоит $10; наконец, если возраст посетителя больше 12, 
# билет стоит $15. Напишите цикл, который предлагает пользователю ввести возраст и выводит цену билета.
while True:
    age = int(input('Enter age:'))
    if age < 3:
        price = 0
    elif 3 < age < 12:
        price = 10
    elif age > 12:
        price = 15
    print('Your price' + ' ' + str(price) + '$')
    break
#7.6
#Три выхода: напишите альтернативную версию упражнения 7-4 или упражнения 7-5, 
# в которой каждый пункт следующего списка встречается хотя бы один раз.
#Завершение цикла по проверке условия в команде while.
#Управление продолжительностью выполнения цикла в зависимости от переменной active.
#Выход из цикла по команде break, если пользователь вводит значение ‘quit’.
active = True
while active:
    message = input('Do you want buy tickets? (Yes/No):')
    if message == 'No' or message == 'no':
        active = False
    else:
        active == True
        age = int(input('Enter age:'))
        if age < 3:
            price = 0
        elif 3 < age < 12:
            price = 10
        elif age > 12:
            price = 15
    print('Your price' + ' ' + str(price) + '$')

#7.7
#Бесконечный цикл: напишите цикл, который никогда не завершается, и выполните его.
#(Чтобы выйти из цикла, нажмите Ctrl+C или закройте окно с выводом.)
while True:
    print('I love you')
    break

#7.8
#Сэндвичи: создайте список с именем sandwich_orders, заполните его названиями различных видов сэндвичей. 
#Создайте пустой список с именем finished_sandwiches. В цикле переберите элементы первого списка и выведите сообщение для каждого элемента 
#(например, «I made your tuna sandwich»). После этого каждый сэндвич из первого списка перемещается в список finished_sandwiches. 
#После того как все элементы первого списка будут обработаны, выведите сообщение с перечислением всех изготовленных сэндвичей.
sandwich_orders = ['reuben', 'monte cristo', 'dagwood']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('I made your', sandwich.title(), 'sandwich')
    finished_sandwiches.append(sandwich)
print('\nСэндвичтер дайын!')
for sandwiches in finished_sandwiches:
    print(sandwiches.title())

#7.9
#Без пастрами: используя список sandwich_orders из упражнения 7-8, проследите за
#тем, чтобы значение ‘pastrami’ встречалось в списке как минимум три раза. Добавьте в начало программы код для вывода сообщения о том,
#что пастрами больше нет, и напишите цикл while для удаления всех вхождений ‘pastrami’ из sandwich_orders. Убедитесь в том, что 
#в finished_sandwiches значение ‘pastrami’ не встречается ни одного раза.
sandwich_orders = ['reuben', 'pastrami', 'monte cristo', 'pastrami', 'dagwood', 'pastrami']
finished_sandwiches = []
print("Өкінішке орай 'pastrami' жоқ.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('I made your', sandwich.title(), 'sandwich')
    finished_sandwiches.append(sandwich)
print('\nСэндвичтер дайын!')
for sandwiches in finished_sandwiches:
    print(sandwiches.title())

#7.10
#Отпуск мечты: напишите программу, которая опрашивает пользователей, где бы они хотели провести отпуск. 
# Включите блок кода для вывода результатов опроса.
holiday_places = []
while True:
    holiday = input("Демалыста қайда барғыңыз келеді? (тоқтату үшін 'quite' енгізіңіз):")
    if holiday == 'quite':
        break
    else:
        holiday_places.append(holiday)
print('Сауалнама нәтижелері:')
for place in holiday_places:
    print('\t', place)