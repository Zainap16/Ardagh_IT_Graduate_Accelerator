import random
word_list = ["elephant","mouse","camel"]

chosen_word = random.choice(word_list)
word = ''.join(chosen_word)
print(word)

guess = input("Guess a letter: ").lower()


for char in word:
    # print(char)
    if guess in char:
        print("yes")
    else:
        print("no")    