'''
CONVERT A LIST OF CHARACTERS INTO A STRING 

Given a list of characters, merge all of them into a string.

Examples:

Input : ['g', 'e', 'e', 'k', 's', 'f', 'o', 
             'r', 'g', 'e', 'e', 'k', 's']
Output : geeksforgeeks 

Input : ['p', 'r', 'o', 'g', 'r', 'a', 'm', 
                        'm', 'i', 'n', 'g']
Output : programming 

'''

S = ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's'] 
print(''.join(S))