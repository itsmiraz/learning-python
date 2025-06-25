# 1. User Info Collector
# Topics: input(), print(), variables, type conversion
# Task:
# Ask the user for their name, age, and height, then print a sentence like:
# "Hello Mirajul! You are 25 years old and 5.9 feet tall."

# Answer

# Irony is i can put any thing in the try else block and add value error execpt and it will catch those type errors 

try : 
    name = str(input('Enter your name : '))

    if not name.isalpha():
        print('Please enter a valid name')

    age = int(input('Enter your age : '))
    if age <10:
        print('Go back to your mommy')
    elif age > 100:
        print('Wow you are a inhuman')    

    height = float(input('Enter your height : '))
    if height > 6 :
        print('Are you an human or alien')
    elif height < 4 :
        print('Why u are soo small')

    print(f"Hello {name}! You are {age} years old and {5.9} feet tall.")

except ValueError as e:
    print(f'Please add number :{e}')




