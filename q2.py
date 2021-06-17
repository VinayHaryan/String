'''
MAXIMUM LENGTH OF CONSECUTIVE 1'S IN A 
BINARY STRING IN PYTHON USING MAP FUNCTION

we are given a binary string containing 1's and 0's.
find maximum length of consecutive 1's in it

Examples:

Input : str = '11000111101010111'
Output : 4


'''

# function to find maximum legth of consecutive 1's in
# a binary string
# def maxconsecutive(Input):
#     # input.split('0') -> splits all sub-string of consecutive 1's
#     # separated by 0's, output will be like['11','1111','1','1','111']
#     # map(len,input.split('0')) -> map function on each
#     # sub-string of consecutive 1's
#     # max() returns maximum element from a list
#     print(max(map(len,input.split('0'))))

# # Driver program
# if __name__ == '__main__':
#     input = '11000111101010111'
#     maxconsecutive(input)

def MAXCONSECUTIVE(INPUT):

    print(max(map(len,INPUT.split('0'))))

# DRIVER FUNCTION
if __name__ == '__main__':
    INPUT = '110001111101010111'
    MAXCONSECUTIVE(INPUT)

# map is built in function that allows you to process
# and transform all the items in an iterable without useing
# an explicit for loop. a technique commonly known as mapping.map()
# is useful when you apply a transfrom function to each item sn iterable 
# and transform them into a new iterable

