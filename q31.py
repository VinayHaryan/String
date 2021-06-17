'''
REMOVE ALL DUPLICATES FROM A GIVEN STRING

We are given a string and we need to remove all duplicates 
from it? What will be the output if the order of character matters?

Examples:

Input : geeksforgeeks
Output : efgkos

'''
from collections import OrderedDict

# function to remove all duplicates from string
# and order does not matter
# def removeduplicatewithoutorder(str):
#     # set() --> A Set is an unordered collection  
#     #         data type that is iterable, mutable,  
#     #         and has no duplicate elements.  
#     # "".join() --> It joins two adjacent elements in  
#     #             iterable with any symbol defined in  
#     #             "" ( double quotes ) and returns a  
#     #             single string  
#     return ''.join(set(str))

# def removeduplicatewithorder(str):
#     return "".join(OrderedDict.fromkeys(str))


# # Driver program 
# if __name__ == "__main__":
#     str = "geeksforgeeks"
#     print("without order= ", removeduplicatewithoutorder(str))
#     print("with order= ", removeduplicatewithorder(str))

def unorder(input):

    return ''.join(set(input))

def order(input):
    return ''.join(OrderedDict.fromkeys(input))

if __name__ == '__main__':
    input = 'geeksforgeeks'
    print("remove duplicate with unorder: ",unorder(input))
    print("remove duplicate with order: ",order(input))