def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10

print("'Ravi' has a hash code: ", hash_function('Ravi'))

# Before: my_hash_set = [None,None,None,None,None,'Bob',None,None,None,None]
# After: my_hash_set = [None,None,Ravi,None,None,'Bob',None,None,None,None]