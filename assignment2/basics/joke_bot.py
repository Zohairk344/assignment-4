JOKE = "Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
PROMPT = "What do you want to hear: "
SORRY = "Sorry I only tell jokes"

def main() :
    user_input = input(PROMPT)
    if user_input.lower() != "joke":
        print(SORRY)
    else :
        print(JOKE)

if __name__ == "__main__":
    main()