'''
REGEX IN PYTHON TO PUT SPACE BETWEEN WORDS STARTING 
WITH CAPITAL LETTERS

Given an array of characters, which is basically a sentence. 
However, there is no space between different words and the 
first letter of every word is in uppercase. 
You need to print this sentence after following amendments:

(i) Put a single space between these words.
(ii) Convert the uppercase letters to lowercase.

Examples:

Input : BruceWayneIsBatman
Output : bruce wayne is batman

Input :  GeeksForGeeks
Output :  geeks for geeks

Approach :

1.Split each word starting with capital letter using re.findall(expression, str) method.

2.Now change capital letter of each word to lowercase and concatenate each word with space.

'''

# import re  
    
# def putSpace(input):  
    
#     # regex [A-Z][a-z]* means any string starting   
#     # with capital character followed by many   
#     # lowercase letters   
#     words = re.findall('[A-Z][a-z]*', input)  
    
#     # Change first letter of each word into lower  
#     # case  
#     result = []  
#     for word in words:  
#         word = chr( ord (word[0]) + 32) + word[1:]  
#         result.append(word)  
#     print (' '.join(result))  
    
# # Driver program  
# if __name__ == "__main__":  
#     input = 'BruceWayneIsBatman'
#     putSpace(input) 

import re
def putspace(input):

    words = re.findall('[A-Z][a-z]*',input)

    result=[]
    for word in words:
        word = chr(ord(word[0]) + 32) + word[1:]
        result.append(word)
    print(' '.join(result))

# Driver program
if __name__ == '__main__':
    input = 'VinayComeFormHaryana'
    putspace(input) 

