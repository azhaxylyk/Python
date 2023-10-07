#4.1
pizza = ['Pepperoni', 'Cheese', 'Hawaiian']
for i in pizza:
    print('I like' + ' ' + i + ' ' + 'pizza.')
print('I really love pizza!')

#4.2
animals = ['Dog', 'Cat', 'Parrot']
for animal in animals:
    print('A' + ' ' + animal + ' ' + 'would  make a great pet.')
print('Any of these animals would make a great pet!')

#4.3
for n in range(21):
    print(n)

#4.5
numbers = list(range(1, 100000))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#4.6
numbers = list(range(1, 21, 2))
for n in numbers:
    print(n)

#4.7
numbers = list(range(3, 31, 3))
for n in numbers:
    print(n)

#4.8
cubes = list(range(1, 11))
for cube in cubes:
    print(cube**3)

#4.9
cubes = [cube**3 for cube in range(1, 11)]
print(cubes)

#4.10
ik = ["Aldik", "Kuka", "Aza", "Zhasik", "Iyuha"]
print("The first three items in the list are:", ik[:3])
print("Three items from the middle of the list are:", ik[2:])
print("The last three items in the list are:", ik[1:4])

#4.11
my_pizzas = ["Пепперони", "Грибная", "4 Сыра"]
friend_pizzas = my_pizzas[:]

friend_pizzas.append("Салями")
my_pizzas.append("Мексиканская")
print("My favorite pizzas are:")
for pizzas in my_pizzas:
    print(pizzas)
print("My friend's favorite pizzas are:")
for pizzas in friend_pizzas:
    print(pizzas)
    
#4.12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append("Картошка")
for foods in my_foods:
    print(foods)
for foods in friend_foods:
    print(foods)
    
#4.13
buffet = ("Coronation chicken scones" "Halloumi fries", "Spring green salad with parsley & blue cheese", 
          "Chicken wing dippers", "Grazing platter")
for dishes in buffet:
    print(dishes)
buffet = ("Coronation chicken scones" "Halloumi fries", "Spring green salad with parsley & blue cheese", 
          "Pull-apart meatball sliders", "Vegetarian sausage rolls")
for dishes in buffet:
    print(dishes)

#4.14

#4.15
import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")

countdown(5)