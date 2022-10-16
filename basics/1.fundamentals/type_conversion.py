# To get input from users use the input() function:
value = input('Enter a value: ')
print(value)

# The input() returns a string and not a number. If you want to get a number value from the user 
#through the input you'll need to convert the type of the input

# To convert a string to a number, use the int() function

price = input('Enter a price ($): ')
tax = input('Enter a tax rate (%): ')

net_price = int(price) - ( int(tax) * int(price) ) / 100
print(f'The net price is ${net_price}')

# MORE TYPE CONVERSIONS
print(int('20'))
print(float('20'))
print(str(20))


# GETTING THE TYPE OF A VALUE
print(type(100))
print(type('100'))
print(type(100.0))
print(type(True))


