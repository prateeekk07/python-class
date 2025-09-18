# OOPs -- 4 pillar
# inheritance -- 
    # - single
    # - multilevel
    # - multiple
    # - hierarchical
    # - hybrid
# polymorphism
# abstraction -- 
# encapsulation -- 

# class A:
#     pass
#     # def m1(self):
#     #     print("in A-m1 method")

# class B(A):
#     pass
#     # def m1(self):
#     #     print("in B-m1 method")

# obj = B()
# obj.m1()
# print(dir(obj))



class A:
    def m1(self):
        print("in A-m1 method")
        # super().m1()

class B(A):
    def m1(self):
        print("in B-m1 method")
        super().m1()

class C(B):
    def m1(self):
        print("in C-m1 method")
        super().m1()


# MRO
# print(C.__mro__)
# obj = C()
# obj.m1()


# class A:
#     def m1(self):
#         print("inside A-m1")

# class B(A):
#     def m1(self):
#         print("inside B-m1")

# class C(A):  # 
#     def m1(self):
#         print("inside C-m1")

# class D(B, C):  # 
#     def m1(self):
#         print("inside D-m1")


# obj = C()
# obj.m1()


class Father:
    def height(self):
        print("height is 5.7")
    def skill(self):
        print("driving")

class Mother:
    def height(self):
        print("height is 5.3")

    def complexion(self):
        print("fair")
    
    def interest(self):
        print("cooking")

class Child(Father, Mother):
    def own_talent(self):
        print("dancing")

# c_obj = Child()
# c_obj.height()
# c_obj.own_talent()
# c_obj.interest()

class Engine:
    def __init__(self, hp, bs_ser="BS6"):
        self.horsepower = hp
        self.bs_series = bs_ser
        print("Initialized Engine")

    def start(self):
        print("Engine start...! vroom vroom")

class Wheels:
    def __init__(self, wc):
        self.wheel_count = wc
        print("Initialized Wheels")

    def rotate(self):
        print("Wheels are rotating..garrr garr ")

class Car(Engine, Wheels):
    def __init__(self, horspwr, whl_count, brand_name, price):
        super().__init__(horspwr) # first preference Engine
        # Engine.__init__(self, horspwr) # explicitely call Wheel's init
        Wheels.__init__(self, whl_count) # explicitely call Wheel's init
        self.brand = brand_name
        self.ex_showroom_price = price
        print("Initialized Car")


    def drive(self):
        self.start()
        self.rotate()
        print(f"{self.brand} is driving smoothly!!")

# obj = Car("1200 cc", 5, "Tata Nexon", "15 lacs")
# obj.drive()


# is a relation and has a relation


class Car:
    pass


class Tata(Car):
    pass

class Hyundai(Car):
    pass


class Vehicle:
    def __init__(self, modname):
        self.model_name = modname


class Engine:
    def __init__(self, hp):
        self.horsepower = hp 

    def __str__(self):
        return f"\n{self.__dict__}"
    
    def __repr__(self):
        return str(self)

class Car(Vehicle):
    def __init__(self, modname, wheel, abgs, prc, hp):
        super().__init__(modname)
        self.wheels = wheel
        self.air_bags = abgs
        self.price = prc
        self.engine = Engine(hp)

    def add_engine(self, eng_obj):  # setter
        self.engine = eng_obj

    def __str__(self):
        return f"\n{self.__dict__}"
    
    def __repr__(self):
        return str(self)

# obj = Engine(150)  # engine object
# car_obj = Car("Tata Nexon", "5 wheels", "6 air bags", "12.50 lacs")
# print(car_obj)
# car_obj.add_engine(obj)
# print(car_obj)


# task -- address, date of birth, employement details


# class Moped(Vehicle):
#     def __init__(self, modname, wheel, diggy, price, mileage):
#         super().__init__(modname)


# class Truck(Vehicle):
#     pass

# lst = [1, 1, 1] # 1
# for i in lst: # 1
#     print("appending", i)
#     lst.append(i)

# print(lst)


class A():  # 
    def m1(self):
        super().m1()
        print("inside A-m1")

class B():  # 
    def m1(self):
        super().m1()
        print("inside B-m1")

class C():  # 
    def m1(self):
        # super().m1()
        print("inside C-m1")

class D(A, B):  # 
    def m1(self):
        super().m1()
        print("inside D-m1")

class E(B, C):  # 
    def m1(self):
        super().m1()
        print("inside E-m1")

class F(D, E):  # 
    def m1(self):
        super().m1()
        print("inside F-m1")

class G(F, E):  # 
    def m1(self):
        super().m1()
        print("inside G-m1")


# obj = G()
# print(G.__mro__)
# obj.m1()


# Create a diamond inheritance scenario:
#         A
#        / \
#       B   C
#        \ /
#         D
# Implement a method process() in A.
# Override in B, C, D using super().
# Call D().process() and explain the order of execution.


class A:
    def process(self):
        print("A.process()")
class B(A):
    def process(self):
        print("B.process()")
        super().process()
class C(A):
    def process(self):
        print("C.process()")
        super().process()
class D(B, C):   # Diamond shape: D inherits from B and C
    def process(self):
        print("D.process()")
        super().process()
# Test
# obj = D()
# obj.process()
# D.process()
# B.process()
# C.process()
# A.process()

# polymorphism


# + 
# print("Py"+"thon")

# duck typing philosphy
# method overloading
# method overriding
# constructor overloding
# operator overloading


class Cat:
    def talk(self):
        print("Meow..Meow!!")

class Human:
    def talk(self):
        print("Hi Hello")

class Duck:
    def talk(self):
        print("Quack quack")
class Bird:
    def chirp(self):
        print("Kukuuukuu")

class Dog:
    def bark(self):
        print("Bow bow")


def call_talk_method(obj):
    if hasattr(obj, "talk"):
        obj.talk()
    elif hasattr(obj, "bark"):
        obj.bark()
    elif hasattr(obj, "chirp"):
        obj.chirp()


# lst = [Cat(), Human(), Duck(), Dog(), Bird()]
# for obj in lst:
#     call_talk_method(obj)


class Duck:
    def quack(self):
        print("Quack, quack!")

    def swim(self):
        print("Duck is swimming.")


class Person:
    def quack(self):
        print("I can also quack like a duck!")

    def swim(self):
        print("I can swim like a duck too!")


def in_the_forest(duckish):
    duckish.quack()
    duckish.swim()


# Using a Duck object
# donald = Duck()
# in_the_forest(donald)

# # Using a Person object (no inheritance from Duck)
# john = Person()
# in_the_forest(john)

# compile-time polymorphism
class A:
    def m1(self): # m1  1 
        print("in m1 with no args")

    def m1(self, a:str): # m1  1 
        pass

    def m1(self, a: int, b: str): # m1 2
        pass

    def m1(self, a, b, c): # m1 3
        pass

    def m1(self, a, b):
        print("in m1")

# obj = A()
# obj.m1()
# method overloading
# "method name, number of arguments, sequnce of arg,  type of argument" -- "signature"


# class A:
#     def m1(self, *args):
#         print(sum(args))


# obj = A()
# obj.m1(1,2,3,4)


class A:
    def m1(self, a=None, b=None, c=None):
        if a and b:
            print(a+b)
        elif b and c:
            print(b+c)
        elif a and c:
            print(a+c)
        elif a and b and c:
            print(a+b+c)
        else:
            print("no arg passed")
# A().m1(b=10, c=2, a=5)

from functools import singledispatch

@singledispatch
def greet(arg):
    print("Hello, something!")

@greet.register
def _(arg: str):
    print(f"Hello, {arg} (string)")

@greet.register
def _(arg: int):
    print(f"Number received: {arg}")

greet("Alice")  # Hello, Alice (string)
greet(42)       # Number received: 42
greet([1,2,3])  # Hello, something!
