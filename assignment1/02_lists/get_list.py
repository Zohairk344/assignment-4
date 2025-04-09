def main():
    List = []
    Data = input("Enter Data to save or leave space blank to cancel: ")
    while Data != "": 
        List.append(Data)
        Data = input("Enter Data to save or leave space blank to cancel: ")
    return print(List)


if __name__ == '__main__':
    main()