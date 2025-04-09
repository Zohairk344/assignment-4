import random

def main():
    Guessed_Number = int(random.randint(0, 99))
    Number = int(input("I am thinking of a number between 0 and 99. Enter a guess: "))
    while Number != Guessed_Number:
        if Number > Guessed_Number:
            print("Your guess is too high")
        if Number < Guessed_Number: 
            print("Your guess is too low")
        Number = int(input("I am thinking of a number between 0 and 99. Enter a guess: "))
    return print(f"Congrats! The number was: {Guessed_Number}")


if __name__ == '__main__':
    main()