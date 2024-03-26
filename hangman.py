import random

word_list = ["elephant","mouse","camel"]
iterate = 0 
tries = 0   
display =[]

chosen_word = random.choice(word_list)
print(chosen_word)

while len(chosen_word) < tries:
    tries += 1
    guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    iterate+=1
    # display.insert(count,letter) 
    display.insert(iterate,"_")
    if guess in letter:
        display.insert(iterate, guess)
    else:
        pass
print(display) 



 
   


        
     
