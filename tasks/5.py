#5.1
me = 'Aknur'
you = 'Aknur'
Aknur = 'Developer'
age = 18
status = 'not in love'

print("Is it me? I predict True.")
print(me == 'Aknur')
print("\nIs it You? I predict False.")
print(me == 'You')
print("\nIs your name Aknur? I predict True.")
print(you == 'Aknur')
print("\nIs yor name Makaka? I predict False.")
print(you == 'Makaka')
print("\nAre you become a developer? I know True.")
print(Aknur == 'Developer')
print("\nAre you unhappy? I know False.")
print(Aknur == 'unhappy')
print("\nAre you adult?")
print(age == 18)
print("\nAre you was adult 1 year ago?")
print(age < 18)


print('\nYou are not fall in love with someone.')
print(status == 'not in love')
print('\nYou are fall in love with someone.')
print(status == 'in love')

#5.2
# Проверка равенства и неравенства строк.
# Проверки с использованием функции lower().
# Числовые проверки равенства и неравенства, условий «больше», «меньше», «больше
# или равно», «меньше или равно».
# Проверки с ключевым словом and и or.
# Проверка вхождения элемента в список.
# Проверка отсутствия элемента в списке.

my_problems = ('Cowardice', 'Fear', 'Envy', 'Loneliness', 'Hatred', 'Laziness', 'Addiction')
my_problem = 'Fear'
problem1 = 'low self-esteem'
problem2 = 'Fear'
number = 7

print(problem1 == my_problem)
print(problem2 == my_problem)
print(problem1 != my_problem)
print(problem2 != my_problem, '\n')
print(problem2.lower() == 'fear')
print(problem1.lower() == 'Low self-esteem', '\n')
print(number == 7)
print(number == 8)
print(number > 7)
print(number < 8)
print(number <= 7)
print(number >= 8, '\n')
print(my_problem == 'Fear' and my_problem == 'fear')
print(number > 5 and number == 7)
print(my_problem == 'Fear' or my_problem == 'fear')
print(number != 7 or number >= 8, '\n')
print(my_problem in my_problems)
print(problem1 in my_problems)
print(problem1 not in my_problems)
print(problem2 not in my_problems)

#5.3
# Цвета 1: представьте, что в вашей компьютерной игре только что был подбит корабль
#пришельцев. Создайте переменную с именем alien_color и присвойте ей значение ‘green’,
#‘yellow’ или ‘red’.
ailen_color = ['green', 'yellow', 'red']
if 'green' in ailen_color:
    print('You have 5 points!')
if 'blue' in ailen_color:
    print('You have 5 points!')

#5.4
ailen_color = ['green', 'yellow', 'red']
if 'green' in ailen_color:
    print('You have 5 points!')
else:
    print('You have 10 points!')

if 'green' not in ailen_color:
    print('You have 10 points!')
else:
    print('You have 5 points!')

#5.5
ailen_color = ['green']
if 'green' in ailen_color:
    print('You have 5 points!')
elif 'yellow' in ailen_color:
    print('You have 10 points!')
else:
    print('You have 15 points!')

ailen_color = ['yellow']
if 'green' in ailen_color:
    print('You have 5 points!')
elif 'yellow' in ailen_color:
    print('You have 10 points!')
else:
    print('You have 15 points!')

ailen_color = ['red']
if 'green' in ailen_color:
    print('You have 5 points!')
elif 'yellow' in ailen_color:
    print('You have 10 points!')
else:
    print('You have 15 points!')

#5.6
age = 18
if age < 2:
    person = 'baby'
elif 2 <= age < 4:
    person = 'kid'
elif 4 <= age < 13:
    person = 'child'
elif 13 <= age < 20:
    person = 'teenager'
elif 20 <= age < 65:
    person = 'adult'
else:
    person = 'oldster'
print(person)

#5.7
#Создайте список трех своих любимых фруктов и назовите его favorite_fruits.
#Напишите пять команд if. Каждая команда должна проверять, входит ли определенный тип фрукта в список. 
# Если фрукт входит в список, блок if должен выводить сообщение вида «You really like bananas!».
favorite_fruits = ['apple', 'banana', 'pear', 'kiwi', 'peach']
if 'apple' in favorite_fruits:
    print('You like apples.')
if 'banana' in favorite_fruits:
    print('You like bananas.')
if 'pear' in favorite_fruits:
    print('YPU like pears.')
if 'kiwi' in favorite_fruits:
    print('You like kiwi.')
if 'peach' in favorite_fruits:
    print('You like peaches.')

#5.8
#Для пользователя с именем 'admin’ выведите особое сообщение — например: «Hello
#admin, would you like to see a status report?»
#Для остальных случаях выводите универсальное приветствие — например: «Hello Eric,
# thank you for logging in again».
names = ['akzhibek', 'mektepbai', 'zhania', 'gali]ya', 'aknur', 'damir', 'admin']
for name in names:
    if name == 'admin':
        print('Hello', ' ', name.title(), ', would you like to see a status report?')
    else:
        print('Hello', name.title(), ', thank you for logging in again')


#5.9
names = []
if names:
    for name in names:
        print('Hello', ' ', name.title(), ', would you like to see a status report?')
else:
    print('We need to find some users!')
    
#5.10
#Создайте список current_users, содержащий пять и более имен пользователей.
#Создайте другой список new_users, содержащий пять и более имен пользователей.
#Убедитесь в том, что одно или два новых имени также присутствуют в списке current_users.
#Переберите список new_users и для каждого имени в этом списке проверьте, было ли оно использовано ранее. 
# Если имя уже использовалось, выведите сообщение о том,что пользователь должен выбрать новое имя. 
# Если имя не использовалось, выведите сообщение о его доступности.
#Проследите за тем, чтобы сравнение выполнялось без учета регистра символов. 
# Если имя 'John’ уже используется, в регистрации имени ‘JOHN’ следует отказать.
current_users = ['akzhibek', 'mektepbai', 'zhania', 'gali]ya', 'aknur', 'damir']
new_users = ['akzhibek', 'mektepbai', 'nursutan', 'nazarbaev', 'abishvsh',]
for name in new_users:
    if name in current_users:
        print('Choose another name.')
    else:
        print('Availabble')

#5.11
for number in range(1, 10):
    if number == 1:
        print(str(number) + 'st')
    elif number == 2:
        print(str(number) + 'nd')
    elif number == 3:
        print(str(number) + 'rd')
    else:
        print(str(number) + 'th')

#5.12
print('YES')

#5.13
print('Для начала, попрбовать создать сайт. В будущем хотелось бы создать приложение, не знаю какое. Может быть что-то типо арка игры.')
