def initFixList():
    with open("wordlist.txt", "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if len(i) > 3:
                f.write(i)
        f.truncate()


totalGuesses = 0

probsDict = {'a': 0.0385, 'b': 0.0385, 'c': 0.0385, 'd': 0.0385, 'e': 0.0385, 'f': 0.0385, 'g': 0.0385, 'h': 0.0385, 'i': 0.0385, 'j': 0.0385, 'k': 0.0385, 'l': 0.0385,
             'm': 0.0385, 'n': 0.0385, 'o': 0.0385, 'p': 0.0385, 'q': 0.0385, 'r': 0.0385, 's': 0.0385, 't': 0.0385, 'u': 0.0385, 'v': 0.0385, 'w': 0.0385, 'x': 0.0385, 'y': 0.0385, 'z': 0.0385, }

countDict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
             'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

countDictRedux = {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1,
                  'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1}

probsDictRedux = {'a': 0.0, 'b': 0.0, 'c': 0.0, 'd': 0.0, 'e': 0.0, 'f': 0.0, 'g': 0.0, 'h': 0.0, 'i': 0.0, 'j': 0.0, 'k': 0.0, 'l': 0.0,
                  'm': 0.0, 'n': 0.0, 'o': 0.0, 'p': 0.0, 'q': 0.0, 'r': 0.0, 's': 0.0, 't': 0.0, 'u': 0.0, 'v': 0.0, 'w': 0.0, 'x': 0.0, 'y': 0.0, 'z': 0.0}


def takeInput():
    global totalGuesses
    global guess
    global countDict
    guess = input("enter")
    if guess != "":
        guess = guess[0]
    if guess in countDict:
        totalGuesses = totalGuesses + 1


def inputLoop():
    while True:
        takeInput()
        updateProbs()
        if guess not in probsDict:
            False
            print(probsDict)
            print("why we stopping tho")
            break


def updateProbs():
    global totalGuesses
    global countDict
    if guess in countDict:
        countDict[guess] = countDict[guess] + 1
        for i in probsDict:
            if totalGuesses > 0:
                probsDict[i] = round((countDict[i] / totalGuesses), 4)


def checksomething():
    total = 0
    for i in probsDict:
        total = total + probsDict[i]
    print(round((total), 3))


inputLoop()
checksomething()
