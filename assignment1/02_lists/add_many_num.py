Numbers = [1,32,5,3,23,324,133,76,56,8,79]

def main(Numbers):
    Total = 0
    for i in range(len(Numbers)) :
        Total = Total + Numbers[i]
    return print(Total)



if __name__ == '__main__':
    main(Numbers)