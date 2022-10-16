# Three logical operators:
# - and
# - or
# - not

print(8 < 10 and 9 > 7) # true
print(8 > 10 and 9 < 7) # false

print(8 < 10 or 9 < 7) # true
print(8 > 10 or 9 < 7) # false

print(not True) # false
print(not False) # true

# PRECEDENCE OF THE LOGICAL OPERATORS
# 1. not (HIGH)
# 2. and (MEDIUM)
# 3. or (LOW)

print(not 8 < 10 or 9 < 7) # false
print(not 8 < 10 or not 9 < 7) # true
print(8 < 10 and 9 > 7) # true
print(8 < 10 and not 9 > 7) # false
print(not 8 > 10 and 9 > 7) # true

