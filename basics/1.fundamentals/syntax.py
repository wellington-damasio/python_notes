# WHITESPACE AND INDENTATION

# Python uses whitespace and indentation to construct code, not ';'

def main():
    i = 1
    max = 10
    while(i < max):
        print(i)
        i = i + 1

main()

# CONTINUATION OF STATEMENTS
# Python uses a newline character to separate statements
# A long statement can span multiple lines by using the backslash (\)
a = 1
b = 0
c = True

if (a == True) and (b == False) and \
    (c == True):
        print("Continuation of statements")

# IDENTIFIERS

# Identifiers are names that identify variables, functions, modules, classes, and other objects 
#in Python

# The name of an identifier needs to begin with a letter or an underscore (_)

# Python identifiers are case-sensitive

# KEYWORDS 

# False      class      finally    is         return
# None       continue   for        lambda     try
# True       def        from       nonlocal   while
# and        del        global     not        with
# as         elif       if         or         yield
# assert     else       import     pass
# break      except     in         raise

# Special module to import keywords in Python
import keyword

print(keyword.kwlist)

# STRING LITERALS
# Python uses quote ('), double quotes ("), triple quotes (''') and triple-double quotes (""") to denote 
#a string literal.

string = 'This is a string'
print(string)

string = "This is a double-quoted string"
print(string)

string = '''
    This string can span across 
    multiple lines
'''
print(string)



