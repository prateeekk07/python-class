# Exception Handling

#try exception

#Error

# logical Error
# Run time Error
# Compile time Error


# try:
#     x = int(input("Enter 1st Number"))
#     y = int(input("Enter 2nd Number"))
#     print(x/y) #risky code
# except ZeroDivisionError:
#     print("Denominator can not be zero") #handler statement
# except ValueError:
#     print("Enter a proper integer")
# else:
#     pass
# finally:
#     print("in finally") #it will appear in all cases whter error is there or not there

# ####################
# print("code is completed")

try:
    l = [10,20,30][5] #IndexError
    print(2/0) #ZeroD
    print(var) #NameError
    print(2/"a") #TypeError
    int("abcf") #ValueError

except IndexError:
    print("no index present")
except ZeroDivisionError:
    print("demo can not be zero")
except NameError as ex:
    print(ex)
except TypeError:
    print("den can be string")
except Exception as ex:
    print(ex)

print("completed")
    
