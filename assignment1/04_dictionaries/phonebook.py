def ReadPhonebook() :
    PhoneBook = {}
    while True :
        Name = input("Name(Leave empty to stop process): ")
        if Name == "": 
            break
        Number = input("Number: ")
        PhoneBook[Name] = Number
    return PhoneBook

def PrintPhoneBook(PhoneBook) :
    for name in PhoneBook: 
        print(f"{name} -> {PhoneBook[name]}")

def LookupNumbers(PhoneBook) :
    while True:
        Name = input("Enter Name to find: ")
        if Name == "":
            break
        if Name not in PhoneBook: 
            print(f"{Name} not found")
        else:
            print(PhoneBook[Name])
        

def main():
    PhoneBook = ReadPhonebook()
    PrintPhoneBook(PhoneBook)
    LookupNumbers(PhoneBook)

 
if __name__ == '__main__':
    main()