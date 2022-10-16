age = input('Enter your age: ')

if int(age) >= 18:
    ticket_price = 20
else:
    ticket_price = 5

print(f"The ticket price is ${ticket_price}")

# You can make if... else more concise by using a ternary operator
name = input('Enter your name: ')

message = f'Você é boboca {name}'  if name != 'Wellington' else 'Você é gostoso'

print(message)

# codition ? value_if_true : value_if_false




