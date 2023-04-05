"""A number-guessing game."""

# Put your code here
import random




def play_game():
    print("Howdy, what is your name?")
    name = input("(type in your name)")
    print(name + " ,I'm thinking of a number between 1 and 100.")
    print("Try to guess my number.")

    secret_number = random.randrange(0,100)
    guess = -1
    count = 0
    best_scores = -1

    def check_play_again():
        nonlocal secret_number, guess, count
        try_again = input("Would you like to play again?")
        if try_again == "Yes" or try_again == "yes":
            secret_number = random.randrange(0,100)
            guess = -1
            count = 0
            return True
        else:
            return False

    while secret_number != guess:
        guess = int(input("Your guess?"))
        count = count + 1
        if secret_number >  guess:
            print("Your guess is too low, try again.")
        elif secret_number <  guess:
            print("Your guess is too high, try again.")
        else:
            if best_scores == -1 or best_scores > count:
                best_scores = count
            print("Well done, {}! You found my number in {} tries! The best scores is {}.".format(name,count,best_scores))
            if not check_play_again():
                break
        if count > 8:
            print("Too many tries!")
            if not check_play_again():
                break

play_game()
    

