#hawaii

vowels = {"a": "ah", "e": "eh", "i": "ee", "o": "oh", "u": "oo"} #dictionary for vowels
the_catch = {"ai": "eye",
             "ae": "eye", #dictionary for double vowels
             "ao": "ow",
             "au": "ow",
             "ei": "ay",
             "eu": "eh-oo",
             "iu": "ew",
             "oi": "oyo",
             "ou": "ow",
             "ui": "ooey",
             }
valid_characters = ["a","e","i","o","u","p","k","h","l","m","n","w"," ", "'"]
#list of valid characters 

def validWord(word):
    #checks the word entered to make sure it contains the valid letters/symbols
    word = word.lower()
    valid = False
    while not valid:
        for char in word:
            if char not in valid_characters:
                print(char, " is not a valid word")
                word = input("Warning, must put a hawaiian word in. Please enter a new word: ")
                word = word.lower()
            else:
                valid = True
                print("valid")
                return word


def hawaiianWord_Convert(word):
    #function to take the validated word and convert it to the hawaiian pronunciation
    validWord(hawaiian_word)
    empty_string = ""
    value = 0
    while value < len(word)-1:
        if word[value] in vowels:
            pair = word[value] + word[value + 1]
            
            if pair in the_catch:
                empty_string += the_catch[pair] + "-"
                value += 2
            else:
                empty_string += vowels[word[value]] + "-"
                value += 1
        else:
            if word[value] == "w":
                if word[value - 1] == "e" or word[value - 1] == "i":
                    if word[value + 1] in vowels:
                        empty_string += "v" + vowels[word[value + 1]] + "-"
                        value += 2
                else:
                    empty_string += word[value] + vowels[word[value + 1]] + "-"
                    value += 2
            elif word[value + 1] in vowels:
                empty_string += word[value] + vowels[word[value + 1]] + "-"
                value += 2

            else:
                empty_string += word[value] + "-"
                value += 1
    return empty_string.strip("-")

def anotherWord():
    #asks the user if he or she wants to test another word 
    another = False
    while not another:
        another_word = input("Do you want to enter another word? (Y/YES/N/NO): ").upper()
        if another_word == "Y" or another_word == "YES":
            hawaiian_word = input("Please enter a hawaiian word: ")
            print(hawaiian_word.upper() + " is pronounced as " + hawaiianWord_Convert(hawaiian_word).capitalize())
        elif another_word == "N" or another_word == "NO":
            another = True
        else:
            print("Please enter a correct response: ")
    

def main():
    #main function to run the program 

    print(hawaiian_word.upper() + " is pronounced as " + hawaiianWord_Convert(hawaiian_word).capitalize())
    anotherWord()
hawaiian_word = input("Please enter a hawaiian word: ").lower()


main()
    

