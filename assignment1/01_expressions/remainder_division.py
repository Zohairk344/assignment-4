def main():
    Num1 = float(input("Enter Number you want divided: "))
    Num2 = float(input("Enter Number you want to divide by: "))
    Total = Num1 / Num2
    Remainder = Num1 // Num2
    return print(f"The answer is {round(Total, 3)} and remainder {Remainder}")


if __name__ == '__main__':
    main()