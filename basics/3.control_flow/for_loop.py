# BASIC LOOP IN PYTHON

# for index in range(n):
#     statement

# index is the loop counter

# The range(n) function generates a sequence of 'n' integers starting from zero. It increases the
# value by one until it reaches 'n'

for index in range(10):
    print(index)

name = 'Lorraine'

name_length = len(name)

for letter_index in range(name_length):
    letter = name[letter_index]
    print(f"{letter_index + 1}: {letter}")

for index in range(99, 109):
    print(index)


for letter_index in range(1, name_length, 2):
    print(name[letter_index])

result = 0

for number in range(1, 106):
    result += number

print(result)


