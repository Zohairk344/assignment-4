def main():
    Year : int = int(input("Enter Year to check if it is leap year: "))
    if Year % 4 == 0 :
        if Year % 100 == 0 : 
            if Year % 400 == 0 :
                print(f"{Year} a leap year!")
            else:
                print(f"{Year} not a leap year.")
        else:
            print(f"{Year} a leap year!")
    else:
        print(f"{Year} not a leap year.")


if __name__ == '__main__':
    main()