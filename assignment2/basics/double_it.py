def main():
    Number = int(input("Enter Number: "))
    Current_Value = Number
    while Current_Value < 100:
        Current_Value = Current_Value * 2
        print(Current_Value)
    print("Number after are greater than 100")



if __name__ == '__main__':
    main()