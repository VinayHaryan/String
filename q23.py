'''
SECOND MOST REPEATED WORD IN A SEQUENCE

Given a sequence of strings, the task is to find out the second 
most repeated (or frequent) string in the given sequence. 
(Considering no two words are the second most repeated, there will be always a single word).

Examples:

Input : {"aaa", "bbb", "ccc", "bbb", 
         "aaa", "aaa"}
Output : bbb

Input : {"geeks", "for", "geeks", "for", 
          "geeks", "aaa"}
Output : for


Approach is very simple –


1.Create a dictionary using Counter(iterator) method which contains 
words as keys and it’s frequency as value.

2.Now get a list of all values in dictionary and sort it in descending order. 
Choose second element from the sorted list because it will be the second largest.

3.Now traverse dictionary again and print key whose value is equal to second largest element.

'''
# from collections import Counter
# def secondfrequent(input):
#     # this sorts from most common to least common to least common
#     c = Counter(input)

#     # c.most_common()[1] prints ('bbb',2)
#     # c.most_common()[1][0] prints output: bbb
#     print(c.most_common()[1][0])

# input = ["geeks", "for", "geeks", "for", 
#           "geeks", "aaa"] 
# secondfrequent(input) 

from collections import Counter
def secondfrequent(input):
    c = Counter(input)
    print(c.most_common()[1][0])

# 
input = ['aaa','bbb','ccc','bbb','aaa','aaa'] 
secondfrequent(input)