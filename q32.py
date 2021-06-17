'''
program to check if a string is palidrome or not

Given a string, write a python function to check if it is palindrome 
or not. A string is said to be palindrome if the reverse of the string 
is the same as string. For example, “radar” is a palindrome, but “radix” 
is not a palindrome.

Examples: 

Input : malayalam
Output : Yes

Input : geeks
Output : No

1.Find reverse of string
2.Check if reverse and original are same or not.


'''
def palindrome(s):
    return s == s[::-1]

# driver function
s = 'malayalam'
ans = palindrome(s)

if ans:
    print("yes")
else:
    print("no")