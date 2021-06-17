'''
USING COUNTER() IN PYTHON TO FIND MINIMUM 
CHARACTER REMOVAL TO MAKE TWO STRINGS ANAGRAM

Given two string in lowercase, the task is to make them anagram.
the only allowed operation is to remove a charcter from any string
find minimum number of characterr to be deleted to make both the string anagram?
if two strings contains same data set in any order then string are called

Anagrams.

Examples:

Input : str1 = "bcadeh" str2 = "hea"
Output: 3
We need to remove b, c and d from str1.

Input : str1 = "cddgk" str2 = "gcd"
Output: 2

Input : str1 = "bca" str2 = "acb"
Output: 0

1.Convert each string into a dictionary data structure using Counter(iterable) method.

2.Count number of keys in both dictionaries ( count1, count2) and count number of keys 
common in both dictionaries

3.If no common keys found that means we need to remove count1 + count2 characters from both 
the strings.

4.Else (max(count1, count2) – countCommon) will be the number of characters to be removed


'''
# # function remove minimum niber of characters so that
# # two string become anagram
# from collections import Counter
# def removechar(str1, str2):

#     # make dictionaries from both strings
#     dict1 = Counter(str1)
#     dict2 = Counter(str2)

#     # extract keys from dict and dict2
#     keys1 = dict1.keys()
#     keys2 = dict2.keys()

#     # count number of keys in both list of keys
#     count1 = len(keys1)
#     count2 = len(keys2)

#     # convert list of keys in set to find common keys
#     set1 = set(keys1)
#     commonkeys = len(set1.intersection(keys2))

#     if (commonkeys == 0):
#         return count1 + count2
#     else:
#         return (max(count1,count2) - commonkeys)

# # driver program 
# if __name__ == '__main__':
#     str1 = 'bcadeh'
#     str2 = 'hea'
#     print(removechar(str1, str2))

from collections import Counter
def REMOVE_CHAR(STR1, STR2):
    
    DICT1 = Counter(STR1)
    DICT2 = Counter(STR2)

    KEYS1 = DICT1.keys()
    KEYS2 = DICT2.keys()

    COUNT1 = len(KEYS1)
    COUNT2 = len(KEYS2)

    SET1 = set(KEYS1)
    COMON_KEYS = len(SET1.intersection(KEYS2))

    if COMON_KEYS == 0:
        return (COUNT1+COUNT2)

    else:
        return (max(COUNT1,COUNT2)-COMON_KEYS)

if __name__ == '__main__':
    STR1 = 'bcadeh'
    STR2 = 'hea'
    print(REMOVE_CHAR(STR1,STR2))