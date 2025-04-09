def main() :
    Adjective = input("Adjective: ")
    Verb1 = input("First Verb: ")
    Verb2 = input("Second Verb: ")
    Famous_Person = input("Enter Name of Famous Person: ")

    MadLib = f"Computer Programming is so {Adjective}! It makes me so excited all the time because \n I Love to {Verb1}. Stay hydrated and {Verb2}! like you are {Famous_Person}!"
    print(MadLib)

if __name__ == "__main__" :
    main()