# To use default parameters, you need to place parameters with default values after those that do not
#have it

def function_name(param1, param2='value2', param3='value3'):
    pass

def greet(name, greeting="Hi"):
    return f"{greeting}, {name}"

print(greet('Wellington'))
print(greet('Isabelle', 'Eaí'))

# DEALING WITH PARAMETER ORDER IN PYTHON FUNCTIONS
def more_greeting(name="There",  message="Hi"):
    return f"{message} {name}"

print(more_greeting("Hello")) # Hi Hello
print(more_greeting(message="Hello")) # Hello There



