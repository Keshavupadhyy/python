user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 20,
}
print('size' in user) # in is used to check whether a key exists in a dictionary.
print('age' in user.keys()) # it's a anthor way to check whether a key exists in a dictionary.
print(user.items()) # The items() method in Python dictionaries returns a view object that displays a list of key-value tuple pairs.
# print(user.clear()) # is clear
user2 = user.copy() # copy the whole dict and create anthor dict and paste in this dict
print(user)
print(user2)
# print(user.pop('age')) # pop is used for remove the key
print(user)
# print(user.popitem()) # popitem is used for remove the last item of the dictionary
print(user.update({'ages': 55})) # is used for the add items in dictionary
print(user)