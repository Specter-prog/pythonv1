'=================== Принципы ООП ================='
# Наследование
# Инкапсуляция
# Полиморфизм
# Абстракция
# Ассоциация (Агрегация, Комопозиция)


'================== Наследование =================='
# Наследование - принцип ООП, в котором мы можем унаследовать, переопределить и использовать в дочернем классе все аттрибуты и методы родительского класса

class A:
    def method(self):
        print('метод в классе А')

obj_a = A()
obj_a.method() # метод в классе А

class B(A):
    pass

obj_b = B()
obj_b.method()


class C(A):
    def method(self):
        print('метод в классе С')
    
obj_c = C()
obj_c.method()


class Animal:
    price = 100000

    def voice(self):
        ...

class Dog(Animal):
    def voice(self):
        return 'bark'

class Cat(Animal):
    def vocie(self):
        return 'meow'

class Duck(Animal):
    def voice(self):
        return 'krya'

Bobik = Dog()
Barsik = Cat()
Donald = Duck()

print(f'Bobik price: {Bobik.price} som, it can {Bobik.voice()}')
print(f'Barsik price: {Barsik.price} som, it can {Barsik.voice()}')
print(f'Donald price: {Donald.price} som, it can {Donald.voice()}')


# одиночное наследование (1 род - 1 дочь)
# иерархическое наследование (1 ряд - много дочь)
class A:
    ...
class B():
    ...

'----------------------------'
class B(A):
    ...

class C(A):
    ...
class D(A):
    ...
'''''''''''''''''''''''''''''''''' множестенное раследловюияя ;игшлря о 1 рлчь'''

class A:
    ...
class C(A, B):
    ...

'--------------------------------'
# многоуровненвое наследование 

class А:
    ...
class C(B):
    ...
class D(C):
    ...
'----------------------'
# гибридное наследование - (смесь видов наследований)
class A:
    ...
class B(A):
    ...
class C(A):
    ...
class E:
    ...
class D(C, E):
    ...

