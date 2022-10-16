number = 1

while number <= 105:
    print(number)
    number += 1

command = ''

while command.lower() != 'quit':
    command = input('>')
    print(f"Echo: {command}")


