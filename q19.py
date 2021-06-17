'''
REMOVE LEADING ZEROS FROM AN IP ADDRESS

given an ip address, remove leading zeros from the ip address

Examples:

Input : 100.020.003.400 
Output : 100.20.3.400

Input :001.200.001.004  
Output : 1.200.1.4

'''

# def removezeros(ip):

#     # splot the ip by "."
#     # convert the words to integers to remove leading removezeors
#     # convert back the integer to string and join them back to a string
#     new_ip = '.'.join([str(int(i)) for i in ip.split(".")])
#     return new_ip

# # driver code
# ip = '100.020.003.400'
# print(removezeros(ip))

def remove_ip(ip):
    
    new_ip = '.'.join([str(int(i)) for i in ip.split('.')])
    return new_ip

# driver function
ip = '001.200.001.004'
print(remove_ip(ip))

