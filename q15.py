'''
PYTHON PROGRAM TO COUNT NUMBER OF VOWELS
USING SETS IN GIVEN STRING

Input : GeeksforGeeks
Output : No. of vowels : 5

Input : Hello World
Output : No. of vowels :  3

APPROCH:
1. Create a set of vowels using set() and initialize a count variable to 0.
2. Traverse through the alphabets in the string and check if the letter in 
the string is present in set vowel.
3. If it is present, the vowel count is incremented.

Below is the implementation of above approach:


'''
# # code to count vowel in
# # a string using set
# # function to count vowel
# def vowel_count(str):
#     # initializing count variable to 0
#     count = 0

#     # creating a set of vowels
#     vowel = set('aeiouAEIOU')

#     # loop to traverse the alphabet
#     # in the given string
#     for alphabet in str:

#         # if alphabet is present 
#         # in set vowel
#         if alphabet in vowel:
#             count = count + 1
#     print("no of vowels :",count)

# # driver code
# str = "vinay"
# vowel_count(str)

def vowel_count(str):
    count = 0
    vowel = set("aioueAIOUE")
    for alpha in str:
        if alpha in vowel:
            count += 1

    print("no of counts: ",count)

# driver function
if __name__ == '__main__':
    str1 = 'vinayharyan'
    vowel_count(str1)