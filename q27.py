'''
STRING SLICING IN PYTHON TO ROTATE A STRING

given a string of size n, write functions to perform following opertions on string

1.Left (Or anticlockwise) rotate the given string by d elements (where d <= n).
2.Right (Or clockwise) rotate the given string by d elements (where d <= n).

Examples:

Input : s = "GeeksforGeeks"
        d = 2
Output : Left Rotation  : "eksforGeeksGe" 
         Right Rotation : "ksGeeksforGee"  


Input : s = "qwertyu" 
        d = 2
Output : Left rotation : "ertyuqw"
         Right rotation : "yuqwert"

1.Separate string in two parts first & second, 
for Left rotation Lfirst = str[0 : d] and Lsecond = str[d :]. 
For Right rotation Rfirst = str[0 : len(str)-d] and Rsecond = str[len(str)-d : ].

2.Now concatenate these two parts second + first accordingly.

'''
# function to rotate string left and right by d length
# def rotate(input,d):

#     # slice string in two parts for left and right
#     Lfirst = input[0:d]
#     Lsecond = input[d:]
#     Rfirst = input[0 : len(input) - d]
#     Rsecond = input[len(input)-d:]

#     # now concatenate two parts together
#     print("left rotation: ",(Lsecond + Lfirst))
#     print("Right Rotation: ",(Rsecond + Rfirst))

# # Driver program
# if __name__ == '__main__':
#     input = 'geeksforgeeks'
#     d = 2
#     rotate(input,d)


def rotate(input,d):

    Lfirst = input[0:d]
    Lsecond = input[d:]
    Rfirst = input[0: len(input) - d]
    Rsecond = input[len(input)-d:]

    print("LEFT SHIFT: ",Lsecond+Lfirst)
    print("RIGHT SHIFT: ",Rsecond+Rfirst)

# driver code
if __name__ == '__main__':
    input = 'qwertyu'
    d = 2
    rotate(input,d)