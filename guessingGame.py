# A small, fun, little function you can run in a command prompt, if you have a pipenvironment created and spun up properly. 
# The function says while 'True'. It is always 'True' by default. The only thing that can cause the loop to turn false, is if the user guesses a specific number.
# This is EXTREMELY basic and doesn't explain any rules of the game or anything like that, but it is just a small demonstration.

def guessing_game():
    while True:
        print('What is your guess?')
        guess = input()

        if guess == '117':
            print("You've correctly guessed the answer!")
            return False
        else:
            print(f'No, {guess} is not the answer, please try again\n')

guessing_game()