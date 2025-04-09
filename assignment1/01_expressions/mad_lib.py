SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my"

def main() :
    Noun = input("Enter Noun: ")
    Adjective = input("Enter Adjective: ")
    Verb = input("Enter Verb: ")
    return print(SENTENCE_START + " " + Noun + " " + Adjective + " " + Verb)

if __name__ == '__main__':
    main()