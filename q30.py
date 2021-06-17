'''
ANAGRAM CHECKING IN PYTHON USING COLLECTIONS COUNTER()

Write a function to check whether two given strings are anagram of each other or not. 
An anagram of a string is another string that contains same characters, 
only the order of characters can be different. 
For example, “abcd” and “dabc” are anagram of each other.

Examples:

Input : str1 = “abcd”, str2 = “dabc”
Output : True

Input : str1 = “abcf”, str2 = “kabc”
Output : False

How dictionary comparison works in python ?
If we have two dictionary data structures in python dict1 = {‘a’:2,’b’:3,’c’:1} 
and dict2 = {‘b’:3,’c’:1,’a’:2} and we compare both of them like dict1=dict2 then 
it will result True. In python ordinary dictionary data structure does not follow 
any ordering of keys, when we compare two dictionaries then it compares three checks 
in order number of keys (if they don’t match, the dicts are not equal), 
names of keys (if they don’t match, they’re not equal) and value of each key (they have to be ‘==’, too).


'''
# from collections import Counter
# def anagram(input1, input2): 
  
#     # Counter() returns a dictionary data 
#     # structure which contains characters  
#     # of input as key and their frequencies 
#     # as it's corresponding value 
#     return Counter(input1) == Counter(input2) 
  
# # Driver function 
# if __name__ == "__main__": 
#     input1 = 'abcd'
#     input2 = 'dcab'
#     print (anagram(input1, input2) )

from collections import Counter
def anagram(input1,input2):
    return Counter(input1) == Counter(input2)

if __name__ == "__main__":
    input1 = 'abcd'
    input2 = 'dcab'
    print(anagram(input1,input2))