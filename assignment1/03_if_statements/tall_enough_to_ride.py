MIN_HEIGHT = 50

def main():
    Height = int(input("Enter your height to check How tall are you.(or leave empty to stop program): "))
    while Height != "" :
        if Height >= MIN_HEIGHT: 
            print("You're tall enough to ride!")
        else :
            print("You're not tall enough to ride, but maybe next year!")
        Height = int(input("Enter your height to check How tall are you.(or leave empty to stop program): "))
    return None

if __name__ == '__main__':
    main()