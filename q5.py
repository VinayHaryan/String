'''
REVERSE STRING IN PYTHON

python string library does'nt support the in-built reverse() as done by
other python containers like list, hence knowing methods to reverse
string can prove to be useful. this article discusses several ways to achive it.

'''
# python code to reverse a string 
# using loop

# def reverse(s):
#     str = ''
#     for i in s:
#         str = i + str
#     return str

# s = 'geeksforgeeks'
# print("the original string is: ", end='')
# print(s)

# print("the reversed string(using loops) is: ", end='')
# print(reverse(s))

def REVERSE(S):
    STR = ''
    for I in S:
        STR = I + STR
    return STR

S = 'GEEKSFORGEEKS'
print("ORIGINAL STRING: ",S)

print("REVERSE STRING: ",REVERSE(S))
