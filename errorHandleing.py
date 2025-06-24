# try : 
#     x = int(input('Enter a number: '))
# except ZeroDivisionError:
#     print('YOu can not divide by zero')
# except ValueError:
#     print('Please enter a valid number')


# try : 
#     file = open('test.txt',"r")
#     content = file.read()
# except FileNotFoundError:
#     print('File not found')
# finally :
#     print('This always runs')
#     if "file" in locals():
#         file.close


def divide (a,b):
    if b==0:
        raise ValueError('B can not be 0')
    return a/b


try:
    result =divide(10,0)
except ValueError as e:
    print(f'Error :{e}')



#     Exception	When It Happens
# ValueError	Invalid value type (e.g., int("abc"))
# TypeError	Wrong type (e.g., 3 + "hello")
# ZeroDivisionError	Dividing by zero
# IndexError	Index out of range in lists
# KeyError	Accessing a missing dict key
# FileNotFoundError	File does not exist
# NameError	Variable not defined
# AttributeError	Wrong attribute used on object