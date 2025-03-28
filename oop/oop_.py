'===================== OOP ====================='
# OOP - Object-orientated programing
# OOП - Объектно ориентированное прогаммирование (парадигма) (способ написания кода)

# class - это шаблоны (типы данных это классы)
# object(instance, экземпляр) - это конечный продукт класса 

class Person:
    # переменные внутри класса (объкта) - аттрибуты
    arms = 2
    legs = 2
    
    def __init__(self, name, age, prof):
        # __init__ - метод, который будет добавлять в объект те аттрибуты, которые у всех объектов разные
        # self - сслыка на объект, который только что создался
        self.name = name
        self.age = age
        self.prof = prof

    # функции внутри класса (объекта) - методы
    def walk(self):
        print(f'{self.name} ходит')

    def swim(self):
        print(f'{self.name} плавает')

obj1 = Person('Katana', 21, 'dev')
obj2 = Person('Nikita', 21, 'dev')
obj3 = Person('Aman', 20, 'senior dev')

obj1.walk()
obj1.swim()
obj1.swim()

print(obj1.arms)

print(obj1.name)
print(obj3.name)
print(obj2.age)


class Calc:
    def add(self, a, b):
        return a + b
    
    def dif(self, a, b):
        return a - b
    
    def mult(self, a, b):
        return a * b
    
    def div(self, a, b):
        return a * b
    
calc = Calc()
print(calc.add(1, 10))
print(calc.dif(10, 5))
print(calc.div(4, 5))
print(calc.div(4, 5))