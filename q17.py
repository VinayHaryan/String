'''
CHECK IF A SUBSTRING IS PRESENT IN A GIVEN STRING

GIVEN TWO STRINGS, CHEACK IF S1 IS THEE IN S2

Examples:

Input : s1 = geeks s2=geeks for geeks
Output : yes

Input : s1 = geek s2=geeks for geeks
Output : yes

We can iteratively check for every word, 
but Python provides us an inbuilt function find() 
which checks if a substring is present in the string, 
which is done in one line.

find() function returns -1 if it is not found, 
else it returns the first occurrence, 
so using this function this problem can be solved.


'''
# FUNCTIOON TO CHECK IF SMALL STRING IS 
# THERE IN BIG STRING
# def check(string, sub_str):
#     if (string.find(sub_str) == -1):
#         print("NO")
#     else:
#         print("YES")

# # driver code 
# string = 'geeks for geeks'
# sub_str = 'geek'
# check(string, sub_str)

def check(s1,s2):
    if s1.find(s2) == True:
        print("No")
    else:
        print("yes")

s1 = 'vinay haryan'
s2 = 'haryan'
check(s1,s2)