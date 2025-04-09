MAX_LENGTH : int = 3
Numbers = [1,32,5,3,23,324,133,76,56,8,79]

def Shorten(lst : list) :
    New_List = lst
    while len(New_List) > MAX_LENGTH :
        last_element = lst.pop()
        print(last_element)
    print(New_List)


def main():
    Shorten(Numbers)


if __name__ == '__main__':
    main()