import unittest


def task_11_1():
    def get_formatted_name(city, country):        
        """Builds a formatted full name"""        
        name = city + ', ' + country        
        return name.title()


    class NameTestCase(unittest.TestCase):    
        """Test for get_formatted_name() function"""            
        
        def test_city_country(self):            
            """City and Country"""            
            formatted_name = get_formatted_name('astana', 'kazakhstan')                  
            self.assertEqual(formatted_name, 'Astana, Kazakhstan')    

    unittest.main()


def task_11_2():
    def get_formatted_name(city, country, population=''):            
        """Builds a formatted full name"""    
        if population:        
            name = city + ', ' + country + ', ' + population    
        else:        
            name = city + ', ' + country            
        return name.title()
    

    class NameTestCase(unittest.TestCase):    
        """Test for get_formatted_name() function"""            

        def test_city_country(self):            
            """City and Country"""            
            formatted_name = get_formatted_name('astana', 'kazakhstan')                  
            self.assertEqual(formatted_name, 'Astana, Kazakhstan')        

        def test_city_country_population(self):        
            """City, Country, Population"""        
            formatted_name = get_formatted_name('berlin', 'germany', '3.645 million')           
            self.assertEqual(formatted_name, 'Berlin, Germany, 3.645 Million') 

        unittest.main()

def task_11_3():
    class Employe():
        '''The class employe'''

        def __init__(self, name, surename, salary):
            self.name = name
            self.surename = surename
            self.salary = salary

        def give_raise(self, raiseExc=''):
            if raiseExc:
                raised = self.salary + raiseExc
            else:
                raised = self.salary = self.salary + 5000
            return raised

    class EmployeTestCase(unittest.TestCase):
        '''Test for Employe class'''

        def setUp(self):
            self.a = Employe('Tom', 'Christian', 20000)

        def test_give_default_raise(self):
            '''Default raise'''
            result = self.a.give_raise()
            self.assertEqual(25000, result)

        def test_give_custom_raise(self):
            '''Custom raise'''
            result = self.a.give_raise(10000)
            self.assertEqual(30000, result)

    unittest.main()




















