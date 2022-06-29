import random
def hangman():
    hang_visual =   ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    words = [ "cat" , "dog" , "rabbit" , "subject" , "name"]
    word = words[ random.randint(0,len(words)-1)]
    wrong= 0
    win = False
    remaining_letters = list(word)
    board= [ "_"] * len(word)
    print("welcome to hangman")

    while wrong < len(hang_visual) - 1:
        char = input("Guess the letter \n")
        if char in remaining_letters:
            index= remaining_letters.index(char)
            board[index]= char
            remaining_letters[index] = "$"
               
        else:
            wrong+=1
        print(" ".join(board))
        e= wrong+1
        print("\n".join(hang_visual[0:e]))

        if "_" not in board:
            print("You win")
            print(" ".join(board))
            win = True
            start_game()
            break
    if not win:
        print("You lose")
        print("The word is " + word)
        start_game()





def start_game():
    instruction = input("Would you like to continue the game? \n press 'c' to continue or 'q' to quit \n ")
    if instruction == "q":
        print("Goodbye")
    elif instruction == "c":
        hangman()
    else:
        print("wrong input")
        start_game()


def start():
    instru = input("Would you like to start the game \n If yes enter y ! \n or else enter n \n")
    if instru == "y":
        hangman()
    elif instru == "n":
        print("Good Bye for now! \n ")
        start()
    else:
        print("Wrong input")
        start()
   
start()


