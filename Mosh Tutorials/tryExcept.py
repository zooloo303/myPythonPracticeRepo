try:
    age = int(input("age: "))
    income = 20000
    risk = income / age
    print(risk)
except ZeroDivisionError:
    print("age cannot be zero")
except ValueError:
    print('not a number')
