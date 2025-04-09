import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    term = 0
    while term <= N_NUMBERS:
        print(str(random.randint(MIN_VALUE, MAX_VALUE)))
        term += 1

if __name__ == '__main__':
    main()
