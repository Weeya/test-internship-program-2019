import sys
answer = []
hint = []
guess = []
wrongAns = []
score = 0
heart = 11

def chooseCategory(number):
    category = ""
    if number == "1":
        category = "astronomy"
    elif number == "2":
        category = "fastfood"
    elif number == "3":
        category = "africa"
    readFile(category)

def readFile(category):
    with open(category +'.txt') as File:
        for line in File:
            answer.append(line.split(':')[0])
            hint.append(line.split(':')[1].rstrip())
        question()
        
def question():
    global heart
    for word in range(len(answer)):
        heart = 11
        print("hint: "+ hint[word])
        guess.append([])

        for i in range(len(answer[word])):
            if isAlphabet(answer[word][i]):
                guess[word].append('_')
            else:
                guess[word].append(answer[word][i])
        print(*guess[word])
        
        for time in range(11):
            guessWord = input(">> ")
            heart -= 1
            checkAns(guessWord.lower(),word)
            if isDone(word):
                break
        print("THE ANSWER IS: " + answer[word] + "\n")
        wrongAns.clear()


def isAlphabet(x):
    if x >= 'a' and x <= 'z':
        return True

def checkAns(guessWord,word):
    global score
    isValid = False
    for i in range(len(answer[word])):
        if guessWord == answer[word][i]:
            guess[word][i] = guessWord
            score += 1
            isValid = True
    if isValid == False:
        wrongAns.append(guessWord)

    print(*guess[word],end="")
    print(" score: " + str(score) + ", remaining life: " + str(heart) + " ,wrong guessed: ", end="")
    print(*wrongAns)
    
def isDone(word):
    for i in range(len(answer[word])):
        if guess[word][i] == '_':
            return False
    print("YOU ARE AMAZING!")
    return True

def main():
    print("Welcome to Hangman!\n1. Astronomy\n2. Fastfood restaurant\n3. African wildlife\nchoose number of category you want to play")
    number = input("\n>>> ")
    chooseCategory(number)
    print("total score: " + str(score))

main()