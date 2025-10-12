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

# from functools import singledispatch

# @singledispatch
# def greet(arg):
#     print("Hello, something!")

# @greet.register
# def _(arg: str):
#     print(f"Hello, {arg} (string)")

# @greet.register
# def _(arg: int):
#     print(f"Number received: {arg}")

# @greet.register
# def _(arg: list):
#     print(f"Hello, {arg} (list)")

# @greet.register
# def _(arg: tuple):
#     print(f"tuple received: {arg}")

# greet("Alice")  # Hello, Alice (string)
# greet(42)       # Number received: 42
# greet([1,2,3])  # 


# class A:
#     def m1(self):
#         print("A-m1")

# class B(A):
#     def m1(self):
#         print("B-m1")

# obj = B()
# obj.m1()



class BookA:
    def __init__(self, pages):
        self.page1 = pages

    def __add__(self, otherbook):
        print(self, otherbook)
        return self.page1 + otherbook.page2

class BookB:
    def __init__(self, pages):
        self.page2 = pages
    
    def __add__(self, otherbook):
        print(self, otherbook)
        return self.page2 + otherbook.page1

# obj1 = BookA(120)
# obj2 = BookB(166)
# print(obj2+obj1)



class Point:
    def __init__(self, x, y):
        self.x = x # 2 4
        self.y = y # 3 5

    # Overload +
    def __add__(self, other): # p1, p2
        return Point(self.x + other.x, self.y + other.y)

    # For pretty printing
    def __str__(self):
        return f"({self.x}, {self.y})"


# p1 = Point(2, 3)
# p2 = Point(4, 5)
# p3 = p1 + p2  # calls p1.__add__(p2)
# print(p3)     # (6, 8)

