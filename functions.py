def greet():
    print('Hello world')


# greet()

def greenByName(name):
    print(f"Hello {name}")


# name = input('Enter a name: ')
# greenByName(name)


def add(a,b):
    return a+b


# r = add(4,5)
# print(r)


def greetGuest(name='Guest'):
    print(f"Hello {name}")


# greetGuest()
# greetGuest("Miraj")


def profile(name,age):
    print(f"Name: {name}, Age:{age}")


# profile(age=20,name='Miraj')


def total_sum(*args):
    print(args)
    return sum(args)


# print(total_sum(1,2,3,4))

def print_info(**kwargs):
    print(kwargs)
    for key ,value in kwargs.items():
        print(f"{key}:{value}")



# print_info(name="Mirajul", age=25)


x = 10

def test():
    x =5
    print('Inside:',x)


# test()
# print("Outside: ",x)

count =0

def increment():
    global count
    count+=1


# increment()
# print(count)
# Write a function to multiply two numbers and return the result.

def multiply_numbers(a,b):
    return a*b

# result = multiply_numbers(1,3)
# print(result)


def calculate_average(*args):
    if len(args)==0:
        return 0
    total = sum(args)
    average = total/len(args)
    return average


print(calculate_average(10,20,30))