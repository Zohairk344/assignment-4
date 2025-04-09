import random

def main():
    Num_of_sides = 6    
    Dice1 = random.randint(1,Num_of_sides)
    print(f"Dice 1 got {Dice1}")
    Dice2 = random.randint(1,Num_of_sides)
    print(f"Dice 2 got {Dice2}")
    Total = Dice1 + Dice2
    return print(f"Total is {Total}")


if __name__ == '__main__':
    main()