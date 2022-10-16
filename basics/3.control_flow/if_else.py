# THE SIMPLE PYTHON IF STATEMENT

# if condition:
#     if-block code

age = input('Enter your age: ')

if int(age) >= 18:
    print('You\'re a grown adult')
    print('Let\'s drink a bit!')
else:
    print('Lorraine falou que você não pode beber')

# PYTHON IF ELSE STATEMENT
is_gay = input("Are you gay? (y = YES, n = NO) ")

if is_gay == 'y':
    print("So you are gay... I see")
    print("Good for your!")
else:
    print("I don't care anyway")
    print("Have a good day!")

# PYTHON ELSE IF (ELIF)
favorite_sport = input('What is your favorite sport? (1 = F1) , (2 = football), (3 = volley) ')

if favorite_sport == '1':
    print('A man with good taste I see...')
elif favorite_sport == '2':
    print('Classical, I respect your taste')
elif favorite_sport == '3':
    print('Awesome! (if you a girl, obviously...)')
else:
    print('Difficult person to please you are.')









