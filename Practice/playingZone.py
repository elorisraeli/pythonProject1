secret_word = "elor"
guess = ""
num_of_guess = 0
guess_limit = 5
out_of_guess = False

while guess != secret_word and not out_of_guess:
    if num_of_guess == 3:
        print("Take a hint -> its the name of the programmer")
    if num_of_guess < guess_limit:
        guess = input("Enter your guess: ")
        num_of_guess += 1
    else:
        out_of_guess = True
if out_of_guess:
    print("Out of guesses, YOU LOSE!")
else:
    print("You Won!")
