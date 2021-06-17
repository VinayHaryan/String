'''
PYTHON GROUPBY METHOD TO REMOVE ALL CONSECUTIVE DUPLICATES

given a string S, remove all the cosecutive duplicates

Input  : aaaaabbbbbb
Output : ab

Input : geeksforgeeks
Output : geksforgeks

Input : aabccba
Output : abcba

Group by method takes input one is iterable (list,tuple,dictionary) and
second is key function which calculates keys for each element present in
itrable. it returns key and iterable of grouped items. if key function  not
specified or is None, key defaults to an identity function and returns the element 
unchanged.

'''
# number = [1, 1, 1, 3, 3, 2, 2, 2, 1, 1] 
# import itertools
# for (key, group) in itertools.groupby(number):
#     print(key,list(group))

numbers = [1, 1, 1, 3, 3, 2, 2, 2, 1, 1]
import itertools

for (key,group) in itertools.groupby(numbers):
    print(key,list(group))


# from itertools import groupby
# def removeallconsecutive(input):
#     # group all consecutive characters based on their
#     # order in string and we are only concerned
#     # about first character of each consecutive substring 
#     # in given string, so key value will work for us
#     # and we will join these keys without space to 
#     # generate resultant string

#     result = []
#     for (key,group) in groupby(input):
#         result.append(key)

#     print(''.join(result))


# # driver program 
# if __name__ == '__main__':
#     input = 'aaaaabbbbbb'
#     removeallconsecutive(input)


from itertools import groupby
def REMOVEDUPLICATE(INPUT):
    RESULT = []
    for (KEY,GROUP) in groupby(INPUT):
        RESULT.append(KEY)
    print(''.join(RESULT))

INPUT = 'VVVVHHHH'
REMOVEDUPLICATE(INPUT)