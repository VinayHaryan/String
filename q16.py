'''
PYTHON SET TO CHECK IF STRING IS PANGRAM

given a string, check if the given string is pangram or not.

Examples:

Input : The quick brown fox jumps over the lazy dog
Output : The string is a pangram

Input : geeks for geeks
Output : The string is not pangram

A normal way would have been to use frequency table and 
check if all elements were present or not. But using import 
ascii_lowercase as asc_lower we import all the lower characters 
in set and all characters of string in another set. 
In the function, two sets are formed- one for all lower case 
letters and one for the letters in the string. 
The two sets are subtracted and if it is an empty set, 
the string is a pangram.

Below is Python implementation of the above approach:


'''
# # import from string all ascii_lowercase and asc_lower
# from string import ascii_lowercase as asc_lower

# # function to check if all elements are present or not
# def check(s):
#     return set(asc_lower) - set(s.lower()) == set([])

# # driver code
# string = 'The quick brown fox jumps over the lazy dog'
# if (check(string)==True):
#     print("the string is a pangram")
# else:
#     print("the string isn't a pangram")

from string import ascii_lowercase as asc_lower
def check(s):
    return set(asc_lower) - set(s.lower()) == set([])
if __name__ == "__main__":
    s = 'The quick brown fox jumps over the lazy dog'
    if (check(s) == True):
        print("pangram")
    else:
        print("not pangram")
        