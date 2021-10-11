#hangman
import random
def importword(): # finding a random word in the dictionary
    file = open("wdd.txt", "r")
    for x in range(0,random.randint(0,466909)):
        word = file.readline(x)
    return word

word = importword()


#####


var = 0
words = []
gues = []




word = word.lower()


lives = int(input("how many lives do you want? \n"))
for x in range(0,len(word)):
    words.append(word[x]) # basically converting the word into an array, with each letter having a position in said array.
    gues.append("_")
words.pop(-1)
gues.pop(-1)
# print(words)


while var < len(words) and lives > 0:
    check = 0
    print(gues)
    guess = input("input letter to guess \n")
    for x in range(0,len(words)):
        if guess == words[x] and gues[x] == "_":
            check = 1
            var += 1
            gues[x] = words[x]
    if check != 1: # if the word wasn't in the array at all, or if you copied a letter, then it'll count it as incorrect
        lives = lives - 1
        print("that letter wasn't in the word, therefore you lost a life. You have", lives, "lives left.")

if lives == 0:
    print("you lost. Restart program to try again")
    print("the word was:")
    print(words)
else:
    print(gues)
    print("you win!")

        
                   
    
