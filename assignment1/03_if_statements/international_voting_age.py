def main():
    Age = input("Enter Age to check in which country you are eligible for voting")
    if Age < 15 :
        print("You can vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.")
    elif Age < 24 :
        print("You can vote in Peturksbouipo where the voting age is 16. You can vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.")
    elif Age < 47 :
        print("You can vote in Peturksbouipo where the voting age is 16. You can vote in Stanlau where the voting age is 25. You can vote in Mayengua where the voting age is 48.")
    else : 
        print("You cannot vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.")


if __name__ == '__main__':
    main()