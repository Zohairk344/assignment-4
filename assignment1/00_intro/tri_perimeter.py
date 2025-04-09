def main():
    Side1 = float(input("Enter Length Of Side1 in cm: "))
    Side2 = float(input("Enter Length Of Side2 in cm: "))
    Side3 = float(input("Enter Length Of Side3 in cm: "))
    Perimeter = Side1 + Side2 + Side3
    return print(f"The Perimeter Of All Sides is {Perimeter}")


if __name__ == '__main__':
    main()