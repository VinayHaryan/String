'''
DICTIONARY AND COUNTER IN PYTHON TO FIND WINNER OF ELECTION

Given an array of names of candidates in an election. a candidate 
name in the array represents a votes cast to the candidate. print the name of
candidates receved max vote. if there is the, print a lexicographically
smaller name

Examples:

Input :  votes[] = {"john", "johnny", "jackie", 
                    "johnny", "john", "jackie", 
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny", 
                    "john"};

Output : John
We have four Candidates with name as 'John', 
'Johnny', 'jamie', 'jackie'. The candidates
John and Johny get maximum votes. Since John
is alphabetically smaller, we print it.

Lexicographical ordering means dictionary order. 
For ex: In dictionary 'ado' comes after 'adieu' because 'o' comes after 'i' in English 
alphabetic system. This ordering is not based on length of the string, 
but on the occurrence of the smallest letter first.

Method 2:
this is shorter method
1. Count the number of votes for each person and stores in a dictionary.
2. Find the maximum number of votes.
3. Find corresponding person(s) having votes equal to maximum votes.
4. As we want output according to lexicographical order, so sort the list and print first element.

The Counter holds the data in an unordered collection, 
just like hashtable objects. The elements here represent the keys and the count as values. 
It allows you to count the items in an iterable list. 
Arithmetic operations like addition, subtraction, intersection, and union can be easily 
performed on a Counter.


'''

# from collections import Counter

# votes =['john','johnny','jackie','johnny','john','jackie', 
#     'jamie','jamie','john','johnny','jamie','johnny','john'] 

# # count the votes for person and stores in the dictionary
# vote_count = Counter(votes)

# # find the maximum number of votes
# max_votes = max(vote_count.values())

# # search for people having maximum votes and store in a list
# lst = [i for i in vote_count.keys() if vote_count[i] == max_votes]

# # sort the list and print lexicographical smallest name
# print(sorted(lst)[0])


from collections import Counter

votes =['john','johnny','jackie','johnny','john','jackie', 
    'jamie','jamie','john','johnny','jamie','johnny','john']  

vote_count = Counter(votes)

max_count = max(vote_count.values())

lst = [i for i in vote_count.keys() if vote_count[i] == max_count]

print(sorted(lst)[0])


 

