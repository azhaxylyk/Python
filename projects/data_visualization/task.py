import matplotlib.pyplot as plt

def task_1():
    "15.1. Кубы: число, возведенное в третью степень, называется «кубом»." 
    "Нанесите на диаграмму первые пять кубов, а затем первые 5000 кубов."
    "15.2. Цветные кубы: примените цветовую карту к диаграмме с кубами"
    x_values = list(range(1, 6))
    y_values = [x**3 for x in x_values]
    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values, c = y_values, cmap=plt.cm.Blues, s = 15)
    ax.set_title("x**3", fontsize=24)
    ax.tick_params(axis='both', which='major', labelsize=14)
    ax.axis([0, 6, 0, 130])
    plt.show()



