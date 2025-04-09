def count_Nums(num_List):
    num_dict = {}
    for n in num_List:
        if n not in num_dict:  # Fix the condition to check num_dict instead of num_List
            num_dict[n] = 1
        else:
            num_dict[n] += 1

    for n in num_dict:
        print(str(n) + " appears " + str(num_dict[n]) + " times.")  # Remove the extra print()

def main():
    Numbers = []
    while True:
        number = input("Enter a number (or leave empty to stop): ")
        if number == "":
            break
        try:
            number = int(number)
            Numbers.append(number)
        except ValueError:
            print("Please enter a valid integer.")
    
    if Numbers:  # Check if the list is not empty
        count_Nums(Numbers)
    else:
        print("No numbers were entered.")

if __name__ == '__main__':
    main()