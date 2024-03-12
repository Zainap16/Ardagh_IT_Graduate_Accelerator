# name = input('what is ur name: ')
# print('hello ' + name)

# year_born = input('what year were you born in: ')
# CURRENTYEAR = 2024
# calc_age = CURRENTYEAR - int(year_born)

# print('your age is: '+str(calc_age))
# string functions, .upper(), .find(''), .replace('','') 
#//
# power to ** 5^2 == 5 ** 2
# modulus %
# x += 3 ==== x = x + 3
# print(5 % 2)

# TEMP = 30

# if TEMP > 30:
#     print("It's a hot day")

# elif TEMP > 20:
#     print("Normal day")
# else:
#     print("It's a cold day LOL")

# i = 0

# while i < 5:
#     i += 1
#     print(i)

# names = ['zainap','colleen','jackie','gintama', 'itachi']
# names[0] = 'Jon'
# print(names[0:3])
# names[0:3] 3 i the index 3
#.append -- >> list methods, insert, remove
# names.insert(0, 'joe')
# print(len(names))

# numbers = [1,2,3,4,5]
# for item in numbers:
#     print(item)

#d research on range()
    # tuples cant be changed
# this is a class
class Robot:
    def intro_self(self):
        print("My name is "+ self.name)
        print("My favorite color is: "+ self.color)
# this is an object
r1 = Robot()
r1.name = "Tom"
r1.color = "red"
r1.weight = 30

r2 = Robot()
r2.name = "Joe"
r2.color = "blue"
r2.weight = 100

r1.intro_self()
r2.intro_self()