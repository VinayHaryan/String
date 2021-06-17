'''
PYTHON CODE TO MOVE SPACES TO FRONT OF STRING
IN SINGLE TRAVERSAL

Given a string that has set of words and spaces, 
write a program to move all spaces to front of string, 
by traversing the string only once.

Examples:

Input  : str = "geeks for geeks"
Output : ste = "  geeksforgeeks"

Input  : str = "move these spaces to beginning"
Output : str = "    movethesespacestobeginning"
There were four space characters in input,
all of them should be shifted in front. 

Approach:

1.Traverse input string and create a string without any space 
character using list comprehension.

2.Now to know how many space characters were there in original 
string just take a difference of length of original string and 
new string.

3.Now create another string and append space characters at the beginning.

'''
# # function to move spaces to front of string
# # in single traversal in python

# def movespaces(input):

#     # traverse string to create string without spaces
#     no_space = [ch for ch in input if ch != ' ']

#     # calculate number of spaces
#     space = len(input) - len(no_space)

#     result = ' '*space
#     # create result string with spaces
#     result = '"'+result+''.join(no_space)+'"'
#     print(result)

# # driver program
# if __name__ == '__main__':
#     input = 'geeks for geeks'
#     movespaces(input)

def movespaces(input):

    nospace = [chr for chr in input if chr != ' ']

    length = len(input) - len(nospace)

    result = ' '*length

    result = '"'+result+''.join(nospace)+'"'
    print(result)

if __name__ == "__main__":
    input = 'vinay from haryana'
    movespaces(input)

