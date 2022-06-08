# Example
"""
(__call__)

class Employee:
    id = 0
    name = ""

    def __init__(self, i, n):
        self.id = i
        self.name = n

    def __call__(self, *args, **kwargs):
        print('printing args')
        print(*args)
        print('printing kwargs')
        for key, value in kwargs.items():
            print("%s == %s" % (key, value))


e = Employee(10, 'Pankaj')  # creating object
print(e)  # printing object
print(callable(e))"""

'''
(__repr__)


class Test:
    def __init__(self, name, salary):
        self.v1 = name
        self.v2 = salary

    def __str__(self):
        return f'User name is {self.v1} and his/her salary is {self.v2}'

    def __repr__(self):
        return f'User(name={self.v1}, salary={self.v2})'


val = Test('Bogdan', 500)
print(val.__str__())
print(val.__repr__())
'''
'''
(classmethod)

class Person:
    age = 25
    
    def print_age(self):
        print('The age is:', self.age)
    # create printAge class method


Person.printAge = classmethod(Person.printAge)
Person.printAge()
'''
'''
(staticmethod)

class Mathematics:
    x = 100
    y = 200

    @staticmethod
    def sum(x, y):
        return x + y
'''
'''
Getter, Setter , Deleter ,Property



class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self, value):
        print('get balanse')
        return self.__balance

    @my_balance.setter
    def set_balance(self, value):
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance == value


r = BankAccount'''
