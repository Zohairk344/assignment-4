def main():
    Sentence = "I am capable of doing anything I put my mind to"
    Answer = input(f"Please type the following affirmation: {Sentence}.: ")
    while Answer.lower() != Sentence.lower():
        print("Hmmm That was not the affirmation.")
        Answer = input(f"Please type the following affirmation: {Sentence}.: ")
    print("I am capable of doing anything I put my mind to. That's right! :)")



if __name__ == '__main__':
    main()