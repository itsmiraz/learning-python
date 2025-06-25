

try :
    inputNumber = int(input("Please enter a number: "))

    if inputNumber % 2 == 0:
        print('Number is Even')
    else :
        print('Number is odd')


except  ValueError as e :

    print(f"Error: {e}")