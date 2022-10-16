# The continue statement skips the current iteration 

# for index in range(n):
#     if condition:
#         continue

for number in range(20):
    if number % 2: # 2, 4, 6 return 0 so it skips the even numbers
        continue

    print(number)


counter = 0

while counter <= 20:
    counter += 1

    if not counter % 2:
        continue

   print(f'Counter: {counter}')






 


