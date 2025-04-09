import random

def play() :
    User = input("choose 'r' for rock, 'p' for paper, 's' for scissor: ")
    Computer = random.choice(['r', 'p', 's'])

    if User.lower() == Computer:
        return "Tie"
    
    if Is_Win(User, Computer) :
        return "You Won"
    return "You Lost"

def Is_Win(Player, Opponent) :
    if (Player == "r" and Opponent == "s") or (Player == "s" and Opponent == "p") or (Player == "p" and Opponent == "r"):
        return True
    
if __name__ == "__main__" :
    print(play())