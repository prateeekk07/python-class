#inheritance
    #-single
    #-multilevel
    #-multiple
    #-hierarchical
    #-hybrid

# class Commonmethod:
#     def __str__(self):
#         return f"\n{self.__dict__}"
    
#     def __repr__(self):
#         return str(self)

# class Student(Commonmethod):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# class Section(Commonmethod):
#     def __init__(self,section,name):
#         self.section = section
#         self.name = name

# s1 = Student("prateek",22)
# s2 = Section("c")

# print(s1)

#Single Inheritance - One child inherits from one parent.

# class Vehicle:
#     def move(self):
#         print("Moving...")

# class Car(Vehicle):  # Car inherits from Vehicle
#     pass
#     # print("not moving")

# c = Car()
# c.move()  # Moving...

#Multiple Inheritance - A child inherits from multiple parents.

# class Flyer:
#     def action(self):
#         print("I can fly")

# class Swimmer:
#     def action(self):
#         print("I can swim")

# class Duck(Flyer, Swimmer):
#     pass

# d = Swimmer()
# d.action()   # I can fly  (method resolution order -> Flyer comes first)

# Multilevel Inheritance - A chain of inheritance.

# class Animal:
#     def eat(self):
#         print("Eating...")

# class Mammal(Animal):
#     def breathe(self):
#         print("Breathing...")

# class Dog(Mammal):
#     def bark(self):
#         print("Woof!")

# dog = Dog()
# dog.eat()      # From Animal
# dog.breathe()  # From Mammal
# dog.bark()     # From Dog

# Hierarchical Inheritance - Multiple children inherit from the same parent.

# class Animal:
#     def speak(self):
#         print("Some sound")

# class Dog(Animal):
#     def speak(self):
#         print("Woof!")

# class Cat(Animal):
#     def speak(self):
#         print("Meow!")

# Dog().speak()  # Woof!
# Cat().speak()  # Meow!

# Hybrid Inheritance - Combination of multiple types. This can get complex.

# class A:
#     def show(self): print("A")

# class B(A): pass
# class C(A): pass
# class D(B, C): pass   # Diamond problem (resolved by MRO)

# print(D.mro())
# # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# Using super() in Inheritance

# super() lets a child call methods from its parent class.
# Important in multiple inheritance, so all classes in the chain cooperate.

# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")
#         super().show()   # calls A.show()

# B().show()
# # B
# # A




# Single inheritance

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound")

# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} barks loudly!")

# # Create an object of Dog
# dog1 = Dog("Buddy")
# dog1.speak()  # inherited method
# dog1.bark()   # child method



class CPU:
    def __init__(self,ram):
        self.ram = ram

    def show_ram(self):
        print({self.ram})
    
class Gaming(CPU):
    def gpu(self,gname):
        self.gname = gname
        print(f"ram = {self.ram} ## gpu = {self.gname}")

c1 = CPU("16gb")

Gaming.gpu("rtx 4070")

        




