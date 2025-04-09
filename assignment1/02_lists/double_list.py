Numbers = [1,32,5,3,23,324,133,76,56,8,79]

def main(Number):
    New_Num = []
    for i in range(len(Number)):
        double_num = Number[i] * 2
        New_Num.append(double_num) 
    return print(New_Num)



if __name__ == '__main__':
    main(Numbers)