def get_factorial(number):
    return number * get_factorial(number - 1)

factorial_of_6 = get_factorial(6)

print(factorial_of_6)
