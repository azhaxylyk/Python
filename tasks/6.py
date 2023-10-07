#6.1
#Человек: используйте словарь для сохранения информации об известном вам человеке. Сохраните имя, фамилию,
#  возраст и город, в котором живет этот человек. Словарь должен содержать ключи с такими именами, 
# как first_name, last_name, age и city. Выведите каждый фрагмент информации, хранящийся в словаре.
person = {'first_name': 'Aknur', 'last_name': 'Zhaxylykova', 'age': 18, 'city': 'Nur-Sultan'}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

#6.2
#Любимые числа: используйте словарь для хранения любимых чисел. Возьмите пять имен 
# и используйте их как ключи словаря. Придумайте любимое число для каждого человека 
# и сохраните его как значение в словаре. Выведите имя каждого человека и его любимое число. 
# Чтобы задача стала более интересной, опросите нескольких друзей и соберите реальные данные 
# для своей программы.
numbers = {'Aknur': 7, 'Taylor': 13, 'Beyonce': 4, 'David': 7, 'Justin': 6, 'Penelopa': 8}
for key, value in numbers.items():
    print(key + ':', value)

#6.3
#Вспомните пять терминов из области программирования, которые вы узнали в предыдущих главах. 
# Используйте эти слова как ключи глоссария, а их определения — как значения.
#Выведите каждое слово и его определение в аккуратно отформатированном виде. Например, вы можете вывести слово,
#  затем двоеточие и определение; или же слово в одной строке, а его определение — с отступом 
# в следующей строке. Используйте символ новой строки (\n) для вставки пустых строк между парами 
# «слово-определение» в выходных данных.
terms = {'print()': 'which prints a statement to the console',
        'len()': 'which calculates the length of a list',
        'str()': 'which converts a value to a string',
        'title()': 'method returns a string where the first character in every word is upper case',
        'strip()': 'method in Python removes or truncates the given characters from the beginning and the end of the original string'
}
for key, value in terms.items():
    print(key + ':', value, '\n')

#6.4
#Глоссарий 2: теперь, когда вы знаете, как перебрать элементы словаря, упростите код из упражнения 6-3, заменив серию 
# команд print циклом, перебирающим ключи и значения словаря. Когда вы будете уверены в том, что цикл работает, добавьте 
# в глоссарий еще пять терминов Python. При повторном запуске программы новые слова и значения должны быть автоматически включены в вывод.
terms = {'print()': 'which prints a statement to the console',
        'len()': 'which calculates the length of a list',
        'str()': 'which converts a value to a string',
        'title()': 'method returns a string where the first character in every word is upper case',
        'strip()': 'method in Python removes or truncates the given characters from the beginning and the end of the original string'
}
terms['range()'] = 'returns a sequence of numbers starting from zero and increment by 1 by default and stops before the given number'
terms['sorted()'] = 'returns a sorted list from the items in an iterable'
terms['sum()'] = 'the sum of all items in an iterable'
terms['set()'] = ' used to convert any of the iterable to sequence of iterable elements with distinct elements'
terms['append()'] = 'adds an item to the end of the list'
for key, value in terms.items():
    print(key + ':', value, '\n')

#6.5
#Реки: создайте словарь с тремя большими реками и странами, по которым протекает каждая река. Одна из возможных пар «ключ—значение» — 
# ‘nile’: ‘egypt’.
#Используйте цикл для вывода сообщения с упоминанием реки и страны — например, «The Nile runs through Egypt.»
#Используйте цикл для вывода названия каждой реки, включенной в словарь.
#Используйте цикл для вывода названия каждой страны, включенной в словарь.
rivers = {'nile': 'egypt', 'ile': 'kazakhstan', 'mississippi': 'usa', 'yangtze': 'china', 'po': 'italy'}
for key, value in rivers.items():
    print('The'+ ' ' + key.title() + ' ' + 'runs through' + ' ' + value.title())
for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())

#6.6
#Опрос: Возьмите за основу код favorite_languages.py (с. 106).
#Создайте список людей, которые должны участвовать в опросе по поводу любимого языка программирования. Включите некоторые имена, 
# которые уже присутствуют в списке, и некоторые имена, которых в списке еще нет.
#Переберите список людей, которые должны участвовать в опросе. Если они уже прошли опрос, выведите сообщение с благодарностью за участие. 
# Если они еще не проходили опрос, выведите сообщение с предложением принять участие.
favorite_languages = {
                    'jen': 'python',
                    'sarah': 'c',
                    'edward': 'ruby',
                    'phil': 'python',
}
names = ['jen', 'sarah', 'edward', 'phil', 'mateen', 'yeonseo']
for name in favorite_languages.keys():
    for namess in names:
        if name in names:
            print(namess.title(),  ', thanks for participate!')
            names.remove(namess)    
for namess in names:     
    print(namess.title() + ' ' + ', please participate!')

#6.7
#Люди: начните с программы, написанной для упражнения 6-1 (с. 107). Создайте два новых словаря, представляющих разных людей, 
# и сохраните все три словаря в списке с именем people. Переберите элементы списка людей. 
# В процессе перебора выведите всю имеющуюся информацию о каждом человеке.
person1 = {'first_name': 'Aknur', 'last_name': 'Zhaxylykova', 'age': 18, 'city': 'Nur-Sultan'}
person2 = {'first_name': 'Zhaniya', 'last_name': 'Zhaxylykova', 'age': 27, 'city': 'Nur-Sultan'}
person3 = {'first_name': 'Galiya', 'last_name': 'Zhaxylykova', 'age': 25, 'city': 'Nur-Sultan'}
people = [person1, person2, person3]
for person in people:
    print(person)

#6.8
#Домашние животные: создайте несколько словарей, имена которых представляют клички домашних животных. 
#В каждом словаре сохраните информацию о виде животного и имени владельца. Сохраните словари в списке с именем pets. 
#Переберите элементы списка. В процессе перебора выведите всю имеющуюся информацию о каждом животном.
kesha = {'species': 'parrot', 'owner': 'me'}
asha = {'species': 'parrot', 'owner': 'me'}
noname = {'species': 'cat', 'owner': 'me'}
pets = [kesha, asha, noname]
for pet in pets:
    print(pet)

#6.9
#Любимые места: создайте словарь с именем favorite_places. Придумайте названия трех мест, которые станут ключами словаря, 
# и сохраните для каждого человека от одного до трех любимых мест. Чтобы задача стала более интересной, опросите нескольких друзей 
# и соберите реальные данные для своей программы. Переберите данные в словаре, выведите имя каждого человека и его любимые места.
favorite_places = {
                    'me': ['Germany', 'South Korea', 'Japan'],
                    'zhaniya': ['Greece', 'Italy', 'Sweden'],
                    'galiya': ['Italy', 'Norway', 'France']
}
for key, value in favorite_places.items():
    print(key +':', value)

#6.10
#Любимые числа: измените программу из упражнения 6-2 (с. 107), чтобы для каждого
#человека можно было хранить более одного любимого числа. Выведите имя каждого человека в списке и его любимые числа.
numbers = {'Aknur': [7, 13, 22],
           'Sharbat': [3, 5, 7], 
           'Symbat': [4, 7, 9],
           'Azhar': [31, 8, 16], 
           'Maira': [19, 7, 13] 
}
for key, value in numbers.items():
    print(key + ':', value)

#6.11
#Города: создайте словарь с именем cities. Используйте названия трех городов в качестве ключей словаря. 
# Создайте словарь с информацией о каждом городе; включите в него страну, в которой расположен город, 
# примерную численность населения и один примечательный факт, относящийся к этому городу. 
# Ключи словаря каждого города должны называться country, population и fact. Выведите название каждого города и всю сохраненную информацию о нем.
cities = {'Nur-sultan': {
                         'sight': ['Bayterek', 'Khan Shatyr', 'Haret Sultan Mosque'], 
                         'location': 'North portion of Kazakhstan',
                         'population': '1.002 million'
        },
          'Baikonur': {'sight': ['Chupa', 'Source', '272 school'],
                        'location': 'Sourth portion of Kazakhstan',
                        'population': '36,175'
        },

          'Kyzylprda': {'sight': ['Aytbay Mechet', 'Kyzylorda Region Museum', 'Akvapark'],
                         'location': 'Sourth portion of Kazakhstan',
                         'population': '234,736'
        }          
}
for city, info in cities.items():
    print(city)
    sights = info['sight']
    print('\tSights:' + ' ' + str(sights))
    print('\tLocation:' + ' ' + info['location'])
    print('\tPopulation:' + ' ' + info['population'])

#6.12
#Расширение: примеры, с которыми мы работаем, стали достаточно сложными, и в них можно вносить разного рода усовершенствования. 
# Воспользуйтесь одним из примеров этой главы и расширьте его: добавьте новые ключи и значения, измените контекст программы
# или улучшите форматирование вывода.
cities = {'Nur-sultan': {'sight': ['Bayterek', 'Khan Shatyr', 'Haret Sultan Mosque'], 
                         'location': 'North portion of Kazakhstan',
                         'population': '1.002 million'
        },
          'Baikonur': {'sight': ['Chupa', 'Source', '272 school'],
                        'location': 'Sourth portion of Kazakhstan',
                        'population': '36,175'
        },

          'Kyzylprda': {'sight': ['Aytbay Mechet', 'Kyzylorda Region Museum', 'Akvapark'],
                         'location': 'Sourth portion of Kazakhstan',
                         'population': '234,736'
        }          
}
cities['Almaty'] = {'sight': ['Shymbulak', 'Koktal', 'Medeo'],
                    'location': 'Sourth portion of Kazakhstan',
                    'population': '1.777 million'
}
del cities['Baikonur']
for city, info in cities.items():
    print(city)
    sights = info['sight']
    print('\tSights:' + ' ' + str(sights))
    print('\tLocation:' + ' ' + info['location'])
    print('\tPopulation:' + ' ' + info['population'])
