def is_palindrome(string):
    # reverse the string
    rev_str = string[::-1]
    # check if the original string and reversed string are same or not
    if string == rev_str:
        return True
    else:
        return False

# test the function
a=input('Enter your string: ')
print(is_palindrome(a))
