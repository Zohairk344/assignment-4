
def Add_Three_Copies(item, list : list) :
    list.append(item)
    list.append(item)
    list.append(item)
    print(list)

def main():
    stuff = []
    item = input("Enter Word you want to copy three times: ")
    print(stuff)
    Add_Three_Copies(item, stuff)


if __name__ == '__main__':
    main()