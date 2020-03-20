import re
import random
from os import system


def freshGame():
    global lifeList
    global x
    global word
    global gameSolved
    global replay

    replay = True
    lifeList = []
    x = 1
    word = "chocolate"
    gameSolved = False


def getNumEnd():
    if int(repr(x)[-1]) == 1:
        if x == 11:
            numEnd = "th"
        else:
            numEnd = "st"
    elif int(repr(x)[-1]) == 2:
        if x == 12:
            numEnd = "th"
        else:
            numEnd = "nd"
    elif int(repr(x)[-1]) == 3:
        if x == 13:
            numEnd = "th"
        else:
            numEnd = "rd"
    else:
        numEnd = "th"
    # print("GetNumEnd")
    return numEnd


def getInput(numEnd):
    global guess
    global x

    prompt = "Enter your " + str(x) + numEnd + " guess: "
    guess = input(prompt)
    if not re.match("^[a-z]*$", guess):
        print("Only letters a-z allowed!")
    elif len(guess) > 1:
        print("Only 1 character allowed!")

    x = x + 1
    # print("GetInput")
    return guess, x


def getWordList(s):
    wordList = []
    for ch in s:
        wordList.append(ch)
    return wordList


def isGuessCorrect(guess):
    timesCorrect = 0
    for ch in getWordList(word):
        if guess == ch:
            timesCorrect = timesCorrect + 1
    # print("isguesscorrect")
    return timesCorrect


def lifeBar(s):
    global lifeList
    i = 0
    if lifeList == []:
        for ch in s:
            lifeList.append("_")
    else:
        for ch in s:
            if ch == guess:
                lifeList[i] = guess
            i = i + 1
    # print("Lifebar")
    print(lifeList)
    return lifeList


def haveWon(s):
    global gameSolved
    if getWordList(word) == lifeBar(word):
        gameSolved = True
        # print("U WON")
    # print("HAvewon")


def clearScoreBoard():
    global lifeList
    lifeList = []
    lifeBar(word)
    # print("Clear Score Board")


def gameEnd():
    x = 1
    # print("GameEnd")
    clearScoreBoard()


def eachTurn():
    getInput(getNumEnd())
    haveWon(lifeBar(word))
    lifeBar(word)
    if isGuessCorrect(guess) > 0:
        system("clear")
        print("You guessed correctly!")
        lifeBar(word)
    else:
        system("clear")
        print("There are no correct guesses!")
        lifeBar(word)
    # print("EachTurn")


def gameLoop():
    system("clear")
    while gameSolved == False:
        eachTurn()
        if gameSolved == True:
            print("You did it! The word was " + word + ".")
            gameEnd()
            break


yesList = ["YES", "Y", "yes", "y"]
noList = ["NO", "N", "no", "n"]


def replayGame():
    global replay
    replayQuestion = input("Do you want to play again? YES or NO: ")
    if replayQuestion in yesList:
        freshGame()
        newWord()
        gameLoop()
    elif replayQuestion in noList:
        replay = False
    else:
        replay = input("Try that again, YES or NO: ")


def askReplayLoop():
    while replay == True:
        replayGame()
        if replay == False:
            print("See you again!")
            break


def newWord():
    global word
    word = random.choice(open("wordlist.txt").readlines())
    word = word[:-1]


freshGame()
gameLoop()
askReplayLoop()
