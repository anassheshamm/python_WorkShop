import random

while True:
    numberToGuess = random.randint(1, 100)
    attempts = 0
    maxattempts = 7
    print("Welcome to the Number Guessing Game!")


    while attempts < maxattempts:
        attempts += 1
        guess = input(f"Attempt {attempts}/{maxattempts}: Enter your guess (1-100) :")
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid integer.")
            attempts -= 1
            continue
        while guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.")
            guess = int(input(f"Attempt {attempts}/{maxattempts}: Enter your guess (1-100): "))
        if guess < numberToGuess:
            print("Too low!")
        elif guess > numberToGuess:
            print("Too high!")  
        else:
            print("#" * 20)
            print(f"Congratulations! You've guessed the number {numberToGuess} correctly in {attempts} attempts!")
            break
    else:
        print(f"Sorry, you've used all your attempts")
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break


