import random
import game_board

COLOR_MASTER = ['red', 'blue', 'black', 'white', 'brown', 'orange', 'purple', 'pink']

max_password_len = 4
max_password_attempts = 4
allow_repeats = False
attempts = 0
board = game_board.GameBoard(max_password_len, max_password_attempts)

rules = []

#Creates a randomized list of colors to act as the game's password
def password_generator():
    password = []
    if not (allow_repeats):
        password = random.sample(COLOR_MASTER, max_password_len)
    else:
        for i in range(max_password_len):
            color = random.choice(COLOR_MASTER)
            if (color in password) and (password.count(color) <= 2):
                password.append(color)

    
    return password

#Makes sure user's guess is the right length and has viable colors    
def valid_moves(user_guess: str):
    if len(user_guess) != max_password_len:
        return False
    if user_guess.lower not in COLOR_MASTER:
        return False
    return True

#Parses the user's guess to see what they got correct. Prints out relevant information and returns false if there are any incorrect guesses
def guess_checker(user_guess, password):
    guess = user_guess.split()
    correct = 0
    false_position = 0
    empty = 0
    for i in range(max_password_len):
        if(guess[i] == password[i]):
            correct += 1
        else:
            if(guess[i] in password):
                false_position += 1
            else:
                empty += 1
    
    if(correct == max_password_len):
        return True
    print("There are " + str(correct) + " correct in the right position")
    print("There are " + str(false_position) + " correct in the wrong position ")
    print()
    return False

#A recursive function that playes through the entirety of the game Mastermind
def game_loop():
    password = password_generator()
    board.display_board()

#REMEMBER TO TAKE OUT THE PASSWORD!!!!
    print(password)
    user_guess = input("Enter your guess: ")

    #repeats prompt until your input is valid
    while not valid_moves(user_guess):
        print("Your input was wrong. Care to try again?")
        print
        user_guess = input("Enter your guess: ")

    #update the text board, and display
    board.update_board(attempts, user_guess)
    board.display_board()

    #If the user's guess is correct, end the game
    if(guess_checker(user_guess, password)):
        finished = True
        print("Code Broken!  You win!!")
        print
        print
        return
    
    #If the user made too many attempts, end the game
    elif(attempts>= max_password_attempts):
        print("Too Bad!  This game is over")
        print("The correct password was: " + password)
        print
        print("Thank you for playing!")
        return
    
    #if the user's guess is wrong, we move to the next line
    else:
        print("Not quite.  Let's try again")
        attempts += 1
        game_loop()
        
    return
                


def main():
    password = password_generator()
    print(password)
    user_guess = input("Enter your guess: ")
    valid_moves(user_guess)
    guess_checker(user_guess, password)
    
    

if __name__ == "__main__": 
    main() 