'''
CONCATENATED STRING WITH UNCOMMON
CHARACTERS IN PYTHON

Two strings are given and you have to modify 1st string such 
that all the common characters of the 2nd string have 
to be removed and the uncommon characters of the 2nd 
string have to be concatenated with uncommon characters 
of the 1st string.

1.Convert both strings into set so that they could have only unique characters. 
Now take intersection of two sets to get common character both strings have.

2.Now separate out those characters in each string which are not common in both 
of them and concatenate the characters.

'''
# function to concatenated string with uncommon
# characters of two strings

# def uncommonconcat(str1,str2):

#     # convert both strings into set
#     set1 = set(str1)
#     set2 = set(str2)

#     # take itersection of two sets to get list of 
#     # common charaters
#     common = list(set1 & set2)

#     # seprate out charcters in each string
#     # which are not common in both strings
#     result = [ch for ch in str1 if ch not in common] + [ch for ch in str2 if ch not in common]

#     # join each character without space to get
#     # final string
#     print(''.join(result))

# # driver program 
# if __name__ == "__main__":
#     str1 = 'aacdb'
#     str2 = 'gafd'
#     uncommonconcat(str1,str2)

def uncommon_(str1,str2):

    set1 = set(str1)
    set2 = set(str2)
    common = set1 & set2

    result = [i for i in str1 if i not in common] + [i for i in str2 if i not in common]

    print(''.join(result))

# driver mode 
if __name__ == "__main__":
    str1 = 'abcs'
    str2 = 'cxzca'
    uncommon_(str1,str2)