'''
REMOVE ALL CONSECUTIVE DUPLICATES FROM THE STRING

given a string s, remove all the consecutive duplicates.
note that this probleam is different from here we keep one
character and remove all subsequent same characters

Examples:

Input  : aaaaabbbbbb
Output : ab

Input : geeksforgeeks
Output : geksforgeks

Input : aabccba
Output : abcba

'''
# Python3 program to remove consecutive  
# duplicates from a given string.  
  
# A iterative function that removes  
# consecutive duplicates from string S  
# def removeDuplicates(S): 
          
#     n = len(S)  
      
#     # We don't need to do anything for  
#     # empty or single character string.  
#     if (n < 2) : 
#         return
          
#     # j is used to store index is result  
#     # string (or index of current distinct  
#     # character)  
#     j = 0
      
#     # Traversing string  
#     for i in range(n):  
          
#         # If current character S[i]  
#         # is different from S[j]  
#         if (S[j] != S[i]): 
#             j += 1
#             S[j] = S[i]  
      
#     # Putting string termination  
#     # character.  
#     j += 1
#     S = S[:j] 
#     return S 
      
# # Driver Code  
# if __name__ == '__main__':  
          
#     S1 = "geeksforgeeks"
#     S1 = list(S1.rstrip()) 
#     S1 = removeDuplicates(S1)  
#     print(*S1, sep = "")  

def removeduplicates(s):

    n = len(s)
    
    if n < 2:
        return

    j = 0
    for i in range(n):
        if (s[j] != s[i]):
            j += 1
            s[j] = s[i]
    
    j += 1
    s = s[:j]
    return s

# driver code 
if __name__ == '__main__':
    s1 = 'geeksforgeeks'
    s1 = list(s1.rstrip())
    s1 = removeduplicates(s1)
    print(*s1,sep='')

# Time Complexity : O(n)
# Auxiliary Space : O(1)

