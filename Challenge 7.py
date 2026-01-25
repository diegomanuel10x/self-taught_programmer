alphabet = list("qwertyuiopasdfghjklzxcvbnm")

print("Hangman")


def hangman(word):
    stages = ["            😊      ",
              "           | H |    ",
              "            | |     ",
              ]
    list1 = list(range(len(word)))
    for let in list1:
        if not stages:
            print("Game Over")
            break

        letter = input("Enter a letter: ").lower()

        if letter not in alphabet:
            print("Enter a valid letter and an isolated number!")
            continue

        if letter not in word:
            print("Incorrect")
            print(stages.pop(0))

        elif letter in word:
            print(word.index(letter))
            print(f"great, the word has {len(word)} letter, you have obtained {word.index(letter) + 1}st|th|nd letter")

        if let == list1[-1]:
            print("you win!")

hangman("good")
