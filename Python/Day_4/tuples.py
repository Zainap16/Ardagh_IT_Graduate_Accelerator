# tuple = collection which is ordered and unchangeable used to group together related data
# student =('Bro',21,'male')

# print(student.count('Bro'))
# print(student.index('male'))

# set = collection which is unordered, unindexed. no duplicates values



# utensils = {"fork", "spoon", "knife"}
# dishes = {"bowls", "plate", "cup"}

# utensils.add("napkin")
# utensils.remove("fork")

# utensils.update(dishes)
# dinner_table= utensils.union(dishes)

# for x in dinner_table:
#     print(x)

# dictionary = a changeable(mutable), unordered collection of unique key: value pairs fast because they use hashing, allow us to access a value quickly

capitals = {'usa': 'washington dc',
            'india':'new dehli',
            'china':'beijing',
            'russia':'moscow'}

# print(capitals['usa'])
print(capitals.keys())
print(capitals.get('Germany'))
print(capitals.values()) #.items()

for key,value in capitals.items():
    print(key, value)







