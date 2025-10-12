class A:
    pass
    # variables:- instance, class level, local
    # methods:- instance, static, class

# access specifier
    # scope of variables

# within the class, outside the class, in subclass
class A:
    def __init__(self):
        self.var1 = 10 # global var within the class, outside the class, in subclass
        self._var2 = 20 # protected variable within the class, outside the class, in subclass
        self.__var3 = 30 # private variable/strictly protected - within the class, no outside the class, not in subclass
                                                            # - outside the class and in sublclass by _classname__variable
    def m1(self):
        print(self.var1)
    
    def m11(self):
        print(self._var2)
    
    def m111(self):
        print(self.__var3)

class B(A):
    def m2(self):
        print(self.var1)
    
    def m22(self):
        print(self._var2)

    def m222(self):
        print(self._A__var3)

# obj = A()
# print(obj.__dict__)
# obj._A__var3 = 50 # _classname__variable
# print(obj._A__var3)
# print(obj.__var3)
# obj.m111()
# obj = B()
# obj.m222()

# name mangling


class MyClass:
    def __init__(self):
        self.__private_attr = 42  # name mangled automatically

    def __private_method(self):
        print("This is a private method")

    def public_method(self):
        print("Public method accessing private attribute:", self.__private_attr)
        self.__private_method()

# obj = MyClass()
# obj.public_method()

# # Direct access will fail:
# print(obj.__private_attr)       # AttributeError
# obj.__private_method()       # AttributeError


# But you can still access with the mangled name:
# print(obj._MyClass__private_attr)  # 42
# obj._MyClass__private_method()     # This is a private method
