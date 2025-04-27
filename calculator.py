def calculator():
    while True:
        try:
            num1 = float(input('Enter first Number: '))
        except ValueError:
            print('Enter a float!')
        try: 
            num2 = float(input('Enter second number: '))
        except ValueError:
            print('Enter a float!')
        opr = int(input('\nChoose an operation: \n1.+ \n2.- \n3.* \n4./ \n5. Quit'))
        if opr == 1:
            result = num1 + num2
            print(f'{num1} + {num2} = {result}')
        elif opr == 2:
            result = num1 - num2
            print(f'{num1} - {num2} = {result}')
        elif opr == 3:
            result = num1 * num2
            print(f'{num1} * {num2} = {result}')
        elif opr == 4:
            try :
                result = num1 / num2
                print(f'{num1} / {num2} = {result}')
            except ZeroDivisionError:
                print("Division by Zero's not possible")
        elif opr ==5:
            print('Thanks for using this calculator!')

calculator()
