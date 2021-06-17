'''
PYTHON CODE TO PRINT COMMON CHARACTERS OF TWO STRINGSI IN 
ALPHABETICAL ORDER

given two string, print all the common characters in lexicographical order
if there are no common letters, print -1. all letters are lower case


Input : 
string1 : geeks
string2 : forgeeks
Output : eegks
Explanation: The letters that are common between 
the two strings are e(2 times), k(1 time) and 
s(1 time).
Hence the lexicographical output is "eegks"

Input : 
string1 : hhhhhello
string2 : gfghhmh
Output : hhh

1.Convert both strings into dictionary data type using Counter(str) method, 
which contains characters of string as key and their frequencies as value.

2.Now find common elements between two strings using intersection ( a&b ) property.

3.Resultant will also be an counter dictionary having common elements as keys 
and their common frequencies as value.

4.Use elements() method of counter dictionary to expand list of keys by their frequency 
number of times.

5.Sort the list and concatenate each character of output list without space to print 
resultant string.

# function


'''
# function to print common charcters of two strings
# in alphabetical order
# from collections import Counter

# def common(str1,str2):

#     # convert both string into counter dictionary
#     dict1 = Counter(str1)
#     dict2 = Counter(str2)

#     # take intersection of these dictionaries
#     commonDict = dict1 & dict2

#     if len(commonDict) == 0:
#         print(-1)
#         return
    
#     # get a list of common elements
#     commonChars = list(commonDict.elements())

#     # sort list in ascending order to print resultant
#     # string on alphabetical order
#     commonChars = sorted(commonChars)

#     # joun charcters without space to produce
#     # resultant string
#     print(''.join(commonChars))

# # Driver program
# if __name__ == '__main__':
#     str1 = 'geeks'
#     str2 = 'forgeeks'
#     common(str1, str2)

from collections import Counter
def COMMON(STR1,STR2):

    DICT1 = Counter(STR1)
    DICT2 = Counter(STR2)

    COMMON_DICT = DICT1 & DICT2

    if len(COMMON_DICT) == 0:
        return -1

    COMON_CHAR = list(COMMON_DICT.elements())

    COMMON_CHAR = sorted(COMON_CHAR)

    print(''.join(COMMON_CHAR))

# DIVER FUNCTION
if __name__ == '__main__':
    STR1 = 'GEEKS'
    STR2 = 'FORGEEKS'
    COMMON(STR1,STR2)