from collections import defaultdict

# Create a defaultdict with default value as int
my_dict = defaultdict(int)

# Accessing a key that doesn't exist
print(my_dict['key1'])  # Output: 0 (default value for int)

# Incrementing a key's value
my_dict['key1'] += 1

# Accessing the key again
print(my_dict['key1'])  # Output: 1 (value incremented)

# Create a defaultdict with default value as list
my_dict2 = defaultdict(list)

# Appending to a list under a key
my_dict2['key2'].append('value1')
my_dict2['key2'].append('value2')

print(my_dict2['key2'])  # Output: ['value1', 'value2']

# Accessing a non-existing key
print(my_dict2['key3'])  # Output: [] (default value for list)

# mySet = set(('a','b','c')) # mySet = {}

# myList= ['a','c','c']
# mySet = list(set(myList))

# print(len(myList))
# print(mySet)




