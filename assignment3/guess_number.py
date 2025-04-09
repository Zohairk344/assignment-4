import random

def main(x) :
    Random_Number = random.randint(1, x)
    Guess = 0
    while Guess != Random_Number : 
        Guess = int(input(f"Guess A number between 1 and {x}: "))
        if Guess < Random_Number :
            print("Guess too low")
        elif Guess > Random_Number :
            print("Guess too high")
    print(f"Correct. The number Was {Random_Number}")

def Computer_Guess(x) :
    Low = 1
    High = x
    Feedback = ""
    while Feedback != "c" :
        if Low != High :
            Guess = random.randint(Low, High)
        else : 
            Guess = Low
        Feedback = input(f"Is {Guess} too high(H), too low(L), or correct(C)").lower()
        if Feedback == "h" :
            High = Guess - 1
        elif Feedback == "c" :
            Low = Guess + 1
    print(f"The Computer Guessed Your Number, it was {Guess}")


if __name__ == "__main__" :
    Computer_Guess(24)    