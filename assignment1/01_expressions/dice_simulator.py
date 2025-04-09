import random

def main():
    for i in range(3):
        dice1 = random.randint(1, 6)  
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        print(f"Total of both dice: {total}")


if __name__ == '__main__':
    main()