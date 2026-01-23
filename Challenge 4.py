import random

nums = random.randrange(0, 100)

list = ["The walking dead", "Entourage", "The sopranos", "The vampire Diaries"]
for i in list:
    print(i)

for num in range (25, 50):
    print(num)

for word in list:
    print(word)
    print(enumerate(list))

x = 1

while x > 0:
    user = input("Guess the number(it is less than 100 and greater than 0): ")

    if user == nums:
        print("Correct")
        play = input("Would u like to continue(y/n)")
        if play == "y":
            continue

        if play == "n":
            break

    else:
        print("Wrong")
        play = input("Would u like to continue(y/n)")
        if play == "n":
            break

        if play == "y":
            continue


