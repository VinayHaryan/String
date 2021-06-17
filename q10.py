'''
MAP FUNCTION AND LAMBDA EXPRESSION IN PYTHON
TO REPLACE CHARACTERS

Given a string S, c1 and c2. Replace character c1 with c2 and c2 with c1.
Examples:

Input : str = 'grrksfoegrrks'
        c1 = e, c2 = r 
Output : geeksforgeeks 

Input : str = 'ratul'
        c1 = t, c2 = h 
Output : rahul

'''
# def Replacechars(input,c1,c2):

#     # create lambda to replace c1 with c2, c2
#     # with c1 and other will reamain same
#     # expression will bw like 'lambda x:
#     # x if (x != c1 and x != c2) else c1 if (x==c2) else c2
#     # and map it onto each character of string
#     newchars = map(lambda x: x if (x != c1 and x != c2) else \
#         c1 if (x==c2) else c2,input)

#     # now join each character without space
#     # to print resultant string
#     print(''.join(newchars))

# # Driver program
# if __name__ == '__main__':
#     input = 'grrksfoegrrks' 
#     c1 = 'e'
#     c2 = 'r'
#     Replacechars(input,c1,c2)

def replace(input,c1,c2):

    newchars = map(lambda x: x if (x != c1 and x != c2) else c1 if (x==c2) else c2, input)

    print(''.join(newchars))

if __name__ == '__main__':
    input = 'grrksfoegrrks'
    c1 = 'e'
    c2 = 'r'
    replace(input,c1,c2)