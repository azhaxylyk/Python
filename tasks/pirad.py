from res import*

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