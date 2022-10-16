# Python interpreter will treat the '\' as special character. If you don't want to do so, use raw 
#strings by typing 'r' before the actual string
raw_string = r'C:\python\bin'
print(raw_string)

# CREATING MULTILINE STRINGS
help_message = '''
Usage: mysql command
    -h hostname
    -d database name
    -u username
    -p password
'''

print(help_message)

# USING VARIABLES IN PYTHON STRINGS WITH f-strings
name = 'Dead Warrior'
message = f'Hi, motherfucker, my name is {name}'
print(message)

# CONCATENATING PYTHON STRINGS
# When you use string literals next to each other, Python automatically concatenates them
greeting = 'Hi' ' There!'
print(greeting)

# To concatenate two string variables use the '+' operator
greeting = 'Good '
time = 'Afternoon'

greeting = greeting + time
print(greeting)

# ACCESSING STRING ELEMENTS
string = 'Python String'
print(string[0]) #P
print(string[3]) #h
print(string[-1]) #g
print(string[-3]) #i

# GETTING LENGTH OF A STRING
string_length = len(string)
print(string_length) #13

# SLICING STRINGS
# Then start and the end are optional. If you omit the start, it defaults to zero. If you omit the end,
#it defaults to the string length

print(string[0:6]) #Python string[start : end]

# PYTHON STRINGS ARE IMMUTABLE
# string[0] = 'J' #ERROR: this object does not support assignment

# If you want to modify a string, you need to create a new one from the existing string.
string = 'J' + string[1:]
print(string)

string = 'P' + string[1:8] + 'p' + string[9:]
print(string)








