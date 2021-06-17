'''
PYTHON DICTIONARY TO FIND MIRROR CHARACTERS IN A STRING

Given a string and number N, we need to mirror the characters from N-th
position up to the length of string in the alphabetical order. in mirror
operation, we change 'a' to 'z','b' to 'y' and soon

Examples:

Input : N = 3
        paradox
Output : paizwlc
We mirror characters from position 3 to end.

Input : N = 6
        pneumonia
Output : pnefnlmrz


We have existing solution for this problem please refer Mirror 
characters of a string link. We can solve this problem in Python 
using Dictionary Data Structure. Mirror value of ‘a’ is ‘z’,’b’ 
is ‘y’ etc, so we create a dictionary data structure and one-to-one 
map reverse sequence of alphabets onto original sequence of alphabets. 
Now traverse characters from length k in given string and change 
characters into it’s mirror value using dictionary.

'''

# function to mirror charcters of string
def mirrorchars(input,k):

    # create dictionary
    original = 'abcdefghijklmnopqrstuvwxyz'
    reverse = 'zyxwvutsrqponmlkjihgfedcba'
    dictchars = dict(zip(original,reverse))

    # separate out string after length k to change
    # characters in mirror
    prefix = input[0:k-1]
    suffix = input[k-1:]
    mirror = ''

    # change into mirror
    for i in range(0, len(suffix)):
        mirror = mirror + dictchars[suffix[i]]

    # concat prefix and mirrored part
    print(prefix+mirror)

# driver program 
if __name__ == '__main__':
    input = 'pneumonia'
    k = 6
    mirrorchars(input,k)
    


