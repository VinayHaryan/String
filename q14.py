'''
PYTHON COUNTER AND DICTIONARY INTERSECTION EXAMPLE
(MAKE A STRING USING DELETION AND REARRAGEMENT)

Given two strings, find if we can make first string from second by deleting 
some characters from second and rearranging remaining characters.

Input : s1 = ABHISHEKsinGH
      : s2 = gfhfBHkooIHnfndSHEKsiAnG
Output : Possible

Input : s1 = Hello
      : s2 = dnaKfhelddf
Output : Not Possible

Input : s1 = GeeksforGeeks
      : s2 = rteksfoGrdsskGeggehes
Output : Possible


1.Convert both string into dictionary using Counter(iterable) method, 
each dictionary contains characters within string as Key and their 
frequencies as Value.

2.Now take intersection of two dictionaries and compare resultant output 
with dictionary of first string, if both are equal that means it is possible 
to convert string otherwise not.


'''
# Python code to find if we can make first string 
# from second by deleting some characters from  
# second and rearranging remaining characters. 
# from collections import Counter
# def makestring(str1,str2):

#     # convert both string into dictionaries
#     # output will be like str1='aabbcc'
#     # dict1={'a':2,'b':2,'c':2}
#     dict1 = Counter(str1)
#     dict2 = Counter(str2)

#     # compare resultant dictionary with first
#     # dictionary comparison first compares keys
#     result = dict1 & dict2

#     # compare resultant dictionary with first
#     # dictionary comparison first compares keys
#     # and then compares their corresponding values
#     return result == dict1

# # driver program 
# if __name__ == '__main__':
#     str1 = 'GeeksforGeeks'
#     str2 = 'rteksfoGrdsskGeggehes'
#     if (makestring(str1,str2)==True):
#         print("Possible")
#     else:
#         print("Not possible")

from collections import Counter
def makestring(str1,str2):

    dict1 = Counter(str1)
    dict2 = Counter(str2)

    result = dict1 & dict2

    return result == dict1

# driver function
if __name__ == '__main__':
    str1 = 'ABHISHEKsinGH'
    str2 = 'gfhfBHkooIHnfndSHEKsiAnG'
    if (makestring(str1,str2) == True):
        print('possibale')
    else:
        print("not possibale")


