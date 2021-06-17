'''
ZIP FUNCTION IN PYTHON TO CHANGE TO A NEW CHARACTER SET

Given a 26 letter character set, which is equivalent to character set of English alphabet i.e. 
(abcd….xyz) and act as a relation. We are also given several sentences and we have to translate 
them with the help of given new character set.

Examples:

New character set : qwertyuiopasdfghjklzxcvbnm
Input : "utta"
Output : geek

Input : "egrt"
Output : code

1.Create a dictionary data structure where we will map original 
character set in english language with new given character set, 
zip(newCharSet,origCharSet) does it for us. 
It will map each character of original character set onto each 
given character of new character set sequentially and return 
list of tuples of pairs, now we convert it into dictionary using dict().

2.Now iterate through original string and convert it into new string.


'''

# # function to change string to a new character

# def newstring(charset,input):

#     # map original character set of english
#     # onto new character set given
#     origCharSet = 'abcdefghijklmnopqrstuvwxyz'
#     mapchars = dict(zip(charset,origCharSet))

#     # iterate through original string and get
#     # characters of original character set
#     changechars = [mapchars[chr] for chr in input]

#     # join characters without character set
#     changechars = [mapchars[chr] for chr in input]

#     # join charcters without space to get new string
#     print(''.join(changechars))

# # Driver program 
# if __name__ == '__main__':
#     charset = 'qwertyuiopasdfghjklzxcvbnm'
#     input = 'utta'
#     newstring(charset,input)


def new_string(charset,input):

    originalcharset = 'abcdefghijklmnopqrstuvwxyz'
    mapchars = dict(zip(charset,originalcharset))
    changechar = [mapchars[chr] for chr in input]
    print(''.join(changechar))

# driver program 
if __name__ == '__main__':
    charset = 'qwertyuiopasdfghjklzxcvbnm'
    input = 'utta'
    new_string(charset,input)