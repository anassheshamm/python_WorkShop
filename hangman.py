import random

words = ["good", "bad" , "ugly"]
random_word = random.choice(words) 
display = ["_"] * len(random_word) # list of _ with the length of the random word
print(' '.join(display)) #space in between
lives = 6

guessed_litter = []


while "_" in display and lives > 0:
    
    guessed = input("please guess a letter :").lower()
    # check if the letter was already guessed
    if guessed in guessed_litter:
        print("already guessed")
        print(f"you have {lives} tries")

        continue
    # add the guessed letter to the list
    guessed_litter.append(guessed)
    if guessed not in random_word:
        lives-=1
    else:
        # update the display list with the guessed letter
        for posititon in range(len(random_word)):
            if random_word[posititon] == guessed:
                display[posititon] = guessed

    print(''.join(display))
    print(f"you have {lives} tries")

if lives == 0:
    print("""
          you lose
          """)
else:
    print("""
          you win
          """)

    

# # guessed = input("please guesse the letter :").lower()

# for letter in random_word:
#     if letter == guessed:
#         print("right")
#     else:
#         print("wrong")
    


