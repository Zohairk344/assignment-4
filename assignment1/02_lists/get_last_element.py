def get_last_item(lst):
    if lst:  
        return lst[-1]
    else:
        return None

def get_lst():
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst()
    last_item = get_last_item(lst)
    if last_item is not None:
        print("The last item is:", last_item)
    else:
        print("The list is empty.")

if __name__ == '__main__':
    main()