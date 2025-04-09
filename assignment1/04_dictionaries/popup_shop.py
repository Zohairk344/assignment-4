def main():
    Total = 0
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5} 
    for i in fruits:    
        Amount = input(f"How Much of {i} would you like: ")
        Total += (fruits[i] * float(Amount))
    return print(Total)



if __name__ == '__main__':
    main()