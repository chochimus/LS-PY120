def divide_first_by_second():
    try:
        first = float(input("enter first digit: "))
        second = float(input("enter second digit: "))
        print(f'result is {first / second}')
    except ZeroDivisionError as e:
        print(f'{e.__class__.__name__}: {e}')
    except ValueError as e:
        print(f'{e.__class__.__name__}: {e}')

divide_first_by_second()