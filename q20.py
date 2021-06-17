'''
COUNT ALL PREFFIXES IN GIVEN STRING WITH GREATEST FREQUENCY

given a string, print and count all predixes in which first alphabet has
greater frequency than secod alphabet

Take two alphabets from the user and compare them. 
The prefixes in which the alphabet given first has 
greater frequency than the second alphabet, 
such prefixes are printed, else the result will be 0.

Examples :

Input : string1 = "geek", 
        alphabet1 = "e", alphabet2 = "k"
Output :
ge
gee
geek
3

Input : string1 = "geek",
        alphabet1 = "k", alphabet2 = "e"
Output :
0

Approach : Take an empty string to store the string values of all 
the prefixes formed. Then check for the alphabet with greater 
frequency than the second alphabet. If no such case is found 
then the result will be 0 prefixes.

Below is the implementation :

'''
# function to print the prefixes
# def prefix(string1, alphabet1, alphabet2):
#     count = 0
#     non_empty_string = ''
#     string2 = list(string1)

#     # loop for iterating the length of 
#     # the string and print the prefixes
#     # and the count of query prefixes.
#     for i in range(0, len(string2)):
#         non_empty_string = non_empty_string + (string2[i])

#         if (non_empty_string.count(alphabet1) >
#             non_empty_string.count(alphabet2)):


#             # print all required prefixes
#             print(non_empty_string)

#             # increment count
#             count += 1

#     # return count of the
#     # required prefixes
#     return(count)

# # driver code
# print(prefix("geeksforgeeks",'e','g'))


def prefix(string1,alphabet1,alphabet2):
    count = 0
    non_empty =''
    string2 = list(string1)

    for i in range(0,len(string2)):
        non_empty = non_empty + (string2[i])

        if (non_empty.count(alphabet1) > non_empty.count(alphabet2)):
            print(non_empty)
            count += 1

    return count

# driver
print(prefix("geeksforgeeks",'e','g')) 
