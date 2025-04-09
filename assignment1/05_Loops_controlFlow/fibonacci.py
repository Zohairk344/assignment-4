MAX_VALUE : int = 10000

def main():
    Current_term = 0
    Next_term = 1
    while Current_term <= MAX_VALUE: 
        print(Current_term)
        Later_Term = Current_term + Next_term
        Current_term = Next_term
        Next_term = Later_Term



if __name__ == '__main__':
    main()