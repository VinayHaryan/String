'''
REVERSE WORDS IN A GIVEN STRING IN PYTHON

We are given a string and we need to reverse words of a given string?

Input : str = geeks quiz practice code
Output : str = code practice quiz geeks

1.Separate each word in given string using split() method of string data type in python.
2.Reverse the word separated list.
3.Print words of list, in string form after joining each word with space using ” “.join() method in python.

'''
# function to reverse words of string
# def rev_sentence(sentence):

#     # first split the string into words
#     words = sentence.split(' ')

#     # then reverse the split string list and join using space
#     reverse_sentence = ' '.join(reversed(words))

#     # finally return the joined string
#     return reverse_sentence

# if __name__ == '__main__':
#     input = "geeks quiz practice code"
#     print(rev_sentence(input))

def rev_sentence(sentence):

    sent = sentence.split(' ')

    reverse = ' '.join(reversed(sent))

    return reverse

if __name__ == '__main__':
    sentence = 'hi hello by'
    print(rev_sentence(sentence))