# The boolean data type has two values: True and False
is_active = True
is_admin = False
print(is_active)
print(is_admin)

# When you compare two numbers, Python returns the result as a boolean value:
print(20 > 10)
print(20 < 10)

# To find out if a value is True or False, you use the bool() function. For example:
print('------ bool Function ------')
print(bool('Hi')) # TRUE
print(bool(0)) # FALSE
print(bool(100)) # TRUE

# FALSY AND TRUTHY VALUES
print("""
    The following are falsy in Python: 
        - 0
        - '' (empty string)
        - False
        - None
        - [] (empty list)
        - () (empty tuple)
        - {} (empty dictionary)
""")

