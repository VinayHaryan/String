'''
PYTHON SORTED() TO CHECK IF TWO STRING ARE ANAGRAM OR NOT


Given two string s1 and s2, check if both the string are anagrams of each other

Examples: 

Input : s1 = "listen"
        s2 = "silent"
Output : The strings are anagrams.


Input : s1 = "dad"
        s2 = "bad"
Output : The strings aren't anagrams.

Python provides a inbuilt function sorted() 
which does not modify the original string, 
but returns sorted string.

Below is the Python implementation of the above approach: 


'''
# function to check if two strings are
# anagram or not
# def check(s1,s2):

#     # the sorted string are checked 
#     if (sorted(s1) == sorted(s2)):
#         print("string are anagrams")
#     else:
#         print("string are't anagrams")

# # driver code
# s1 = 'listen'
# s2 = 'silent'
# check(s1,s2)

def check(s1,s2):
    if (sorted(s1) == sorted(s2)):
        print("string is anagrams")
    else:
        print("string is not anagrams")
# driver code
s1 = 'dad'
s2 = 'bad'
check(s1,s2)




