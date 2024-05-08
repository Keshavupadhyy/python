'''
In Python, when you define a dictionary with duplicate keys,
the second assignment overwrites the value of the first assignment.
This is because dictionary keys must be unique, and Python dictionaries
'''
dictionary = {
    '123': [1,2,3],
    '123': 'hello',
    '123': 'keshav',
}
print(dictionary['123'])