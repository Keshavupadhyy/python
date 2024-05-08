'''
Python dictionaries support several methods for performing various operations.
Here are some commonly used dictionary methods:
'''

user = {
    'basket':[1,2,3],
    'greet': 'hello',
}
print(user.get('age',22)) ## Retrieving value for a non-existent key

user2 = dict(name= 'keshav') # its a second way to create a dictionary but commonly used dictionary is upper side
print(user2)
