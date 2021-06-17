'''
SEQUENCE MATCHER IN PYTHON FOR LONGEST COMMON SUBSTRING

Given two strings ‘X’ and ‘Y’, print the longest common sub-string.

Examples:

Input :  X = "GeeksforGeeks", 
         Y = "GeeksQuiz"
Output : Geeks

Input : X = "zxabcdezy", 
        Y = "yzabcdezx"
Output : abcdez

How SequenceMatcher.find_longest_match(aLow,aHigh,bLow,bHigh) method works ?

First we initialize SequenceMatcher object with two input string str1 and str2, 
find_longest_match(aLow,aHigh,bLow,bHigh) takes 4 parameters aLow, bLow are start 
index of first and second string respectively and aHigh, bHigh are length of first 
and second string respectively. find_longest_match() returns named tuple (i, j, k) 
such that a[i:i+k] is equal to b[j:j+k], if no blocks match, this returns (aLow, bLow, 0).

'''
# # function to find logest common sub-string
# from difflib import SequenceMatcher

# def logestsubstring(str1,str2):

#     # initialize sequencematcher object with
#     # input string
#     seqmatch = SequenceMatcher(None,str1,str2)

#     # find match of logest sub-string
#     # output will bw like match(a=0,b=0,size=5)
#     match = seqmatch.find_longest_match(0, len(str1), 0, len(str2))

#     # print logest substring
#     if (match.size != 0):
#         print(str1[match.a:match.a+match.size])
#     else:
#         print('No logest common sub-string found')

# # Driver program

# if __name__ == '__main__':
#     str1 = 'GeeksforGeeks'
#     str2 = 'GeeksQuiz'
#     logestsubstring(str1,str2)

from difflib import SequenceMatcher
def logestsubstring(str1,str2):

    # initialize sequencematcherobject with 
    # input string

    seqmatch = SequenceMatcher(None,str1,str2)

    match = seqmatch.find_longest_match(0,len(str1),0,len(str2))

    if (match.size != 0):
        print(str1[match.a:match.a+match.size])

    else:
        print("no logest common sub-string found")

# Driver program 
if __name__ == '__main__':
    str1 = 'vinayharyanvinay'
    str2 = 'vinayvinu'
    logestsubstring(str1,str2)
    