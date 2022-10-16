# DEFINING A PYTHON FUNCTION
def greet(greeting_message):
    """Display a greeting to users"""
    print(greet.__doc__)
    print(greeting_message)

greet('Hi, motherfucker')

# PARAMETER VS ARGUMENT

# Parameter is a piece of information the function needs to executes its task. Ex: greet(message)

# Argument is the actual data you into the function. Ex: greet('This message')

# RETURNING A VALUE

def sum(number1, number2):
    return number1 + number2

print(sum(23, 11))

difficult_sum = sum(23121, 4452)

print(difficult_sum)

