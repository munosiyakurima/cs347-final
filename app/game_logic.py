import random

COLOR_MASTER = ['red', 'blue', 'black', 'white', 'brown', 'orange', 'purple', 'pink']

max_password_len = 4
max_password_attempts = 4
allow_repeats = False

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
    
def valid_moves(user_guess):
    if len(user_guess) != max_password_len:
        return False
    if user_guess not in COLOR_MASTER:
        return False

def guess_checker(user_guess, password):
    guess = user_guess.split()
    hint = ""
    correct = ""
    false_position = ""
    empty = ""
    
    for i in range(max_password_len):
        if(guess[i].equals(password[i])):
            correct += "cc"
        else:
            if(guess[i] in password):
                false_position += "ff"
            else:
                empty += "e"
    hint = correct + false_position + empty
    print("There are "+ correct.length + " correct")
    print("There are " + false_position.length + " in the wrong position")
    return hint
                


def main():
    password = password_generator()
    print(password)
    user_guess = input("Enter your guess: ")
    valid_moves(user_guess)
    guess_checker(user_guess, password)
    
    

if __name__ == "__main__": 
    main() 