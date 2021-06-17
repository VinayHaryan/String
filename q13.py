'''
PRINT THE INITIALS OF A NAME WITH LAST NAME IN FULL

given a name, print the initials of a name(uppercase)
with last name(with first alphabet in uppercase) written
in full separated by dots

Examples:

Input : geeks for geeks
Output : G.F.Geeks

Input : mohandas karamchand gandhi
Output : M.K.Gandhi 

A naive approach of this will be to iterate for spaces and 
print the next letter after every space except the last space. 
At last space we have to take all the characters after the last 
space in a simple approach.

Using Python in inbuilt functions we can split the words into a list, 
then traverse till the second last word and print the first character 
in capitals using upper() function in python and then add the last word 
using title() function in Python which automatically converts the first 
alphabet to capital.

'''
# # python program to print initials of a name
# def name(s):

#     # split the string into a list
#     l = s.split()
#     new = ''

#     # traverse in the list
#     for i in range(len(l) - 1):
#         s = l[i]

#         # add the capital first character
#         new += (s[0].upper()+'.')
#     # l[-1] gives last item of list l. we
#     # use title to print first character in 
#     # capital
#     new += l[-1].title()
#     return new

# # driver code
# s = 'mohandas karamchand gandhi'
# print(name(s))

def sort_name(name):

    v = name.split()
    new = ''
    for i in range(len(v)-1):
        s = v[i]
        new += (s[0].upper()+'.')

    new += v[-1].title()

    return new

name = 'vinava shinava tinva'
print(sort_name(name))
