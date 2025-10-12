#polymorphism

    # - duck typing philosphy
    # - method overloading
    # - method overriding
    # - constructor overloading
    # - operator overloading

# - duck typing philosphy  

class Cat:
    def talk(self):
        print("Meow..meow!!")

class Human:
    def talk(self):
        print("Hello")

class Duck:
    def talk(self):
        print("Quack Quack")

class Bird:
    def chrip(self):
        print("kukukuk")

class Dog:
    def brak(self):
        print("Bow bow")

def call_talk_method(obj):
    if hasattr(obj,"talk"):
        obj.talk()
    elif hasattr(obj, "bark"):
        obj.bark()
    elif hasattr(obj, "chirp"):
        obj.chirp()

lst = [Cat(),Human(),Duck(),Dog(),Bird()]
for obj in lst:
    call_talk_method(obj)
