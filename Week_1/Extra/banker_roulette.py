import random
# select a random name from a list of names

names = ["Zainap","Kopano","Collen","Shaqeel","Sino"]

names_len = len(names)
rando_names = random.randint(0,names_len - 1)
choice = names[rando_names]
print(f"original list: {names}")
print(f"length of list: {names_len}")
print(f"random element number in the list: {rando_names}")
print(f"{choice} is going to buy the meal today!")











