'''
GENERATE TWO OUTPUT STRING DEPENDING UPON OCCURRENCE OF
CHARACTER IN INPUT STRING IN PYTHON

given an input string str[], generate two strings. one of which 
consists of those character which occurs only once in input string and
second which consists of multi-time occurring charcters. output strings
must be sorted

Examples:

Input : str = "geeksforgeeks"
Output : String with characters occurring once:
"for".
String with characters occurring multiple times:
"egks"

Input : str = "geekspractice"
Output : String with characters occurring once:
"agikprst"
String with characters occurring multiple times:
"ce"

1.Convert string into dictionary having characters as keys and 
their frequencies as value using counter() method.
2.Now separate out list of characters having frequency 1 and having frequency more than 1.
3.Sort characters in both lists to get output strings.

'''
# function Generate two output strings depending upon
# occurrence of character in input string

# from collections import Counter
# def generatestring(input):
#     # convert string into dictionary
#     # having characters as keys and frequency as value
#     freqdict = Counter(input)

#     # separate out characters having frequency 1 and more than 1
#     freq1 = [key for (key,count) in freqdict.items() if count==1]
#     freqmore1 = [ key for (key,count) in freqdict.items() if count > 1]

#     # sort list and concatenate characters 
#     # with out space to print resultant strings
#     freq1.sort()
#     freqmore1.sort()

#     # print output strings
#     print('string with characters occurring once: ' )
#     print(''.join(freq1))
#     print("string with characters occurring multiple times: ")
#     print(''.join(freqmore1))

# # driver program 
# if __name__ == '__main__':
#     input = 'geeksforgeeks'
#     generatestring(input)

from collections import Counter
def GENERATESTRINGS(INPUT):

    STRING_DICT = Counter(INPUT)

    FREQ1 = [KEY for (KEY,COUNT) in STRING_DICT.items() if COUNT == 1]
    FREQMORE1 = [KEY for (KEY,COUNT) in STRING_DICT.items() if COUNT > 1]
    
    FREQ1.sort()
    FREQMORE1.sort()

    print ('STRING APPEAR ONE TIME: ')
    print (''.join(FREQ1))

    print("\nSTRING APPEAR MORE THAN ONE: ")
    print(''.join(FREQMORE1))


# DRIVER PROGRAM 
if __name__ == '__main__':
    INPUT = 'GEEKSFORGEEKS'
    GENERATESTRINGS(INPUT)