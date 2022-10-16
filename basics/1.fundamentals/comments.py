# BLOCK COMMENTS

# This is a block comments

# Python inline comments
price = 'R$' '20.00' #This is an inline comment
print(price)

# DOCSTRINGS

# A documentation string is a string literal that you put as the first line in a code block, for
#example, a function

# Typically, you use a documentation strin to automatically generate the code documentation

# 1) One-line docstrings
def quicksort():
    """sort the list using quicksort algorithm"""
    print(quicksort.__doc__)

quicksort()

# 2) Multi-line docstrings
def increase(salary, percentage, rating):
    """
increase salary based on rating and percentage:
    rating 1 - 2: no increase
    rating 3 - 4: increase 5%
    rating 4 - 6: increase 10%
    """
    print(increase.__doc__)

increase(2000, 10, 2)





