import random
from art import *

tprint("   COLOR GAME   ")

print("🟥🟥🟥🟥🟥🟥🟥🟧🟧🟧🟧🟧🟧🟧🟨🟨🟨🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩🟦🟦🟦🟦🟦🟦🟦")

name = input("\nWhat is your name? ")
print ("\nInstructions: \nIn this game", name,"you don't have to see colors to guess, but guess them on how they are described")
print ("\nNote: \nAll answers should be written in a lowercase format \nexample : black")
print ("\nGood luck ", name, "\n")

print ("🟥🟥🟥🟥🟥🟥🟥🟧🟧🟧🟧🟧🟧🟧🟨🟨🟨🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩🟦🟦🟦🟦🟦🟦🟦")



startGame = input("\nAre you ready? (Y/N) ")

#Hints
red = ("\n-------- 📖 Hint: It can be a color that dracula is attracted to--------", "\n-------- 📖 Hint: it can be a color of an apple --------",
       "\n-------- 📖 Hint: can be a color that can be seen from a tree", "\n-------- 📖 Hint: It can also be known as seductive color --------",
       "\n-------- 📖 Hint: It can be a color of love --------",
       "\n-------- 📖 Hint: It can be a color of anger --------", "\n-------- 📖 Hint : It can be a color from a sauce --------",
       "\n-------- 📖 Hint: It can be a warm color! --------")

green = ("\n-------- 📖 Hint: It is a color that depicts nature --------",
         "\n-------- 📖 Hint: It is a chill and relaxing color --------",
         "\n-------- 📖 Hint: It can also be from a tree --------", "\n-------- 📖 Hint: It is where naruto lives you can see this color a lot --------",
         "\n-------- 📖 Hint: It could be a color of an apple --------", "\n-------- 📖 Hint: This color is considerably ZEN --------")

yellow = ("\n-------- 📖 Hint: It's a bright color --------", "\n-------- 📖 Hint: It is warm but a happy color --------",
          "\n-------- 📖 Hint: It can be a color from a fruit --------", "\n-------- 📖 Hint: It is a color from a sun --------",
          "\n-------- 📖 Hint: Mustard! --------")

orange = ("\n-------- 📖 Hint: It is a color that depicts citrus --------", "\n-------- 📖 Hint: It is a color from a sun --------",
          "\n-------- 📖 Hint: It is a relaxing color --------", "\n-------- 📖 Hint: Naruto's old jacket color --------",
          "\n-------- 📖 Hint: It is the most common color of a ball --------")

blue = ("\n-------- 📖 Hint: Basically a color when we look up --------", "\n-------- 📖 Hint: A color that is reflected from the sea --------",
        "\n-------- 📖 Hint: A color that depicts fluidity --------", "\n-------- 📖 Hint: A professional color --------",
        "\n-------- 📖 Hint: It is a cool color --------")

violet = ("\n-------- 📖 Hint: Dark color --------", "\n-------- 📖 Hint: A color that depicts being a villain --------",
          "\n-------- 📖 Hint: A color that can also be found in fruits --------", "\n-------- 📖 Hint: A color of void --------",
          "\n-------- 📖 Hints : It is kind of a bad color --------")

black = ("\n-------- 📖 Hint: It is the color of your friend's humor --------", "\n-------- 📖 Hint: It's color is associated with death --------",
         "\n-------- 📖 Hint: It's the opposite of light --------")


#Color section
randomColor = ['red', 'blue', 'green', 'yellow', 'orange','violet', 'black']
random.choice(randomColor)

#Change how many turns
turns = 10
score = 0

if startGame == "N":
    print("OKAY")
    exit()

if startGame == "Y" :

    while turns >= 0:
        while random.choice(randomColor) == 'red':
            while True :
                print(random.choice(red))
                guessColor = input("\nWhat color? ")
                if guessColor == 'red':
                    print("____________________________________________________________")
                    print("| CORRECT the answer is color RED, here is your PRICE : 🍎 |")
                    print("____________________________________________________________")
                    print("🟥🟥🟥🟥🟥🟥🟥🟧🟧🟧🟧🟧🟧🟧🟨🟨🟨🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩🟦🟦🟦🟦🟦🟦🟦")
                    score += 1
                    if score == 1:
                        print("SCORE:", score, "point")
                    elif score > 1:
                        print("SCORE:", score, "points")
                    startGame = input("Do you want to play again (Y/N)? ")
                    print("❤ Lives left: ", turns)
                    if startGame == "Y":
                        break
                    if startGame == "N":
                        print("Thank you for playing")
                        exit()
                if guessColor != 'red':
                    turns -= 1
                    print("❤ Lives left: ", turns)
                    if turns == 0:
                        print("SCORE:", score)
                        print("GAME OVER the answer is color RED")
                        exit()
                    continue

        while random.choice(randomColor) == 'blue':
            while True :
                print(random.choice(blue))
                guessColor = input("\nWhat color? ")
                if guessColor == 'blue':
                    print("_____________________________________________________________")
                    print("| CORRECT the answer is color BLUE, here is your PRICE : 💧 |")
                    print("_____________________________________________________________")
                    print("🟥🟥🟥🟥🟥🟥🟥🟧🟧🟧🟧🟧🟧🟧🟨🟨🟨🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩🟦🟦🟦🟦🟦🟦🟦")
                    score += 1
                    if score == 1:
                        print("SCORE:", score, "point")
                    elif score > 1:
                        print("SCORE:", score, "points")
                    startGame = input("Do you want to play again (Y/N)? ")
                    print("❤ Lives left: ", turns)
                    if startGame == "Y":
                        break
                    if startGame == "N":
                        print("Thank you for playing")
                        exit()
                if guessColor != 'blue':
                    turns -= 1
                    print("❤ Lives left: ", turns)
                    if turns == 0:
                        print("SCORE:", score)
                        print("💀 GAME OVER the answer is color BLUE")
                        exit()
                    continue

        while random.choice(randomColor) == 'green':
            while True :
                print(random.choice(green))
                guessColor = input("\nWhat color? ")
                if guessColor == 'green':
                    print("______________________________________________________________")
                    print("| CORRECT the answer is color GREEN, here is your PRICE : 🍏 |")
                    print("______________________________________________________________")
                    print("🟥🟥🟥🟥🟥🟥🟥🟧🟧🟧🟧🟧🟧🟧🟨🟨🟨🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩🟦🟦🟦🟦🟦🟦🟦")
                    score += 1
                    if score == 1:
                        print("SCORE:", score, "point")
                    elif score > 1:
                        print("SCORE :", score, "points")
                    startGame = input("Do you want to play again (Y/N)? ")
                    print("❤ Lives left: ", turns)
                    if startGame == "Y":
                        break
                    if startGame == "N":
                        print("Thank you for playing")
                        exit()
                if guessColor != 'green':
                    turns -= 1
                    print("❤ Lives left: ", turns)
                    if turns == 0:
                        print("SCORE:", score)
                        print("💀 GAME OVER the answer is color GREEN")
                        exit()
                    continue

        while random.choice(randomColor) == 'yellow':
            while True :
                print(random.choice(yellow))
                guessColor = input("\nWhat color? ")
                if guessColor == 'yellow':
                    print("_______________________________________________________________")
                    print("| CORRECT the answer is color YELLOW, here is your PRICE : 🍌 |")
                    print("_______________________________________________________________")
                    print("🟥🟥🟥🟥🟥🟥🟥🟧🟧🟧🟧🟧🟧🟧🟨🟨🟨🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩🟦🟦🟦🟦🟦🟦🟦")
                    score += 1
                    if score == 1 :
                        print("SCORE:", score, "point")
                    elif score > 1 :
                        print("SCORE:", score, "points")
                    startGame = input("Do you want to play again (Y/N)? ")
                    print("❤ Lives left: ", turns)
                    if startGame == "Y":
                        break
                    if startGame == "N":
                        print("Thank you for playing")
                        exit()
                if guessColor != 'yellow':
                    turns -= 1
                    print("❤ Lives left: ", turns)
                    if turns == 0:
                        print("SCORE:", score)
                        print("💀 GAME OVER the answer is color YELLOW")
                        exit()
                    continue

        while random.choice(randomColor) == 'orange':
            while True :
                print(random.choice(orange))
                guessColor = input("\nWhat color? ")
                if guessColor == 'orange':
                    print("_______________________________________________________________")
                    print("| CORRECT the answer is color ORANGE, here is your PRICE : 🍊 |")
                    print("_______________________________________________________________")
                    print("🟥🟥🟥🟥🟥🟥🟥🟧🟧🟧🟧🟧🟧🟧🟨🟨🟨🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩🟦🟦🟦🟦🟦🟦🟦")
                    score += 1
                    if score == 1:
                        print("SCORE:", score, "point")
                    elif score > 1:
                        print("SCORE:", score, "points")
                    startGame = input("Do you want to play again (Y/N)? ")
                    print("❤ Lives left: ", turns)
                    if startGame == "Y":
                        break
                    if startGame == "N":
                        print("Thank you for playing")
                        exit()
                if guessColor != 'orange':
                    turns -= 1
                    print("❤ Lives left: ", turns)
                    if turns == 0:
                        print("SCORE:", score)
                        print("💀 GAME OVER the answer is color ORANGE")
                        exit()
                    continue

        while random.choice(randomColor) == 'violet':
            while True:
                print(random.choice(violet))
                guessColor = input("\nWhat color? ")
                if guessColor == 'violet':
                    print("_______________________________________________________________")
                    print("| CORRECT the answer is color VIOLET, here is your PRICE : 🍆 |")
                    print("_______________________________________________________________")
                    print("🟥🟥🟥🟥🟥🟥🟥🟧🟧🟧🟧🟧🟧🟧🟨🟨🟨🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩🟦🟦🟦🟦🟦🟦🟦")
                    score += 1
                    if score == 1:
                        print("SCORE:", score, "point")
                    elif score > 1:
                        print("SCORE:", score, "points")
                    startGame = input("Do you want to play again (Y/N)? ")
                    print("❤ Lives left: ", turns)
                    if startGame == "Y":
                        break
                    if startGame == "N":
                        print("Thank you for playing")
                        exit()
                if guessColor != 'violet':
                    turns -= 1
                    print("❤ Lives left: ", turns)
                    if turns == 0:
                        print("SCORE: ", score)
                        print("💀 GAME OVER the answer is color VIOLET")
                        exit()
                    continue

        while random.choice(randomColor) == 'black':
            while True:
                print(random.choice(black))
                guessColor = input("\nWhat color? ")
                if guessColor == 'black':
                    print("______________________________________________________________")
                    print("| CORRECT the answer is color BLACK, here is your PRICE : 🖤 |")
                    print("______________________________________________________________")
                    print("🟥🟥🟥🟥🟥🟥🟥🟧🟧🟧🟧🟧🟧🟧🟨🟨🟨🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩🟦🟦🟦🟦🟦🟦🟦")
                    score += 1
                    if score == 1:
                        print("SCORE:", score, "point")
                    elif score > 1:
                        print("SCORE:", score, "points")
                    startGame = input("Do you want to play again (Y/N)? ")
                    print("❤ Lives left: ", turns)
                    if startGame == "Y":
                        break
                    if startGame == "N":
                        print("Thank you for playing")
                        exit()
                if guessColor != 'black':
                    turns -= 1
                    print("❤ Lives left: ", turns)
                    if turns == 0:
                        print("SCORE:", score)
                        print("💀 GAME OVER the answer is color BLACK")
                        exit()
                    continue


else :
    print ("INVALID INPUT")







