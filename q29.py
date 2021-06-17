'''
RUN LENGTH ENCODING IN PYTHON

given an input string, write a function that returns 
string for the input string

For example, if the input string is ‘wwwwaaadexxxxxx’, 
then the function should return ‘w4a3d1e1x6’.

Examples:

Input  :  str = 'wwwwaaadexxxxxx'
Output : 'w4a3d1e1x6'

'''
# python code for run length encoding
# from collections import OrderedDict
# def runlength(input):

#     # generate ordered dictionary of all lower
#     # case alphabets, its output will be
#     # dict = {'w':0, 'a':0, 'd':0, 'e':0, 'x':0} 
#     dict = OrderedDict.fromkeys(input,0)

#     # now iterate through input string to calculate
#     # frquency of each character, its output will be
#     # dict = {'w':4,'a':3,'d':1,'e':1,'x':6} 
#     for ch in input:
#         dict[ch] += 1

#     # now iterate through dictionary to make
#     # output string from (key,value) pairs
#     output = ''
#     for key,value in dict.items():
#         output = output + key + str(value)
#     return output

# # Driver function
# if __name__ == '__main__':
#     input="wwwwaaadexxxxxx"
#     print (runlength(input)) 


from collections import OrderedDict
def runlengthencoding(input):

    dict = OrderedDict.fromkeys(input,0)

    for ch in input:
        dict[ch] += 1

    output = ''
    for key, value in dict.items():
        output = output + key + str(value)
    return output

# Driver function
if __name__ == '__main__':
    input = 'wwwwaaadexxxxxx'
    print(runlengthencoding(input))