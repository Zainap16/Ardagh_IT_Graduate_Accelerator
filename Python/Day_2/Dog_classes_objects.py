# this is a class
class Dog:
    def dog_speaks(self): #this is an init function & 
        # reprsents the instance of a class(objects - class istances)
        # methods - functions
        # attributes - variables
        print('name: '+ self.name)
        print('legs: '+ str(self.legs))
        print('bark')
        
# objects below

d1 = Dog()
d1.name = 'Lola'
d1.legs = 4

# display the d1 info
d1.dog_speaks()
