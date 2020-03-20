from collections import OrderedDict


def removeDuplicates(string):
    result = []
    seen = set()
    for char in string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)


wordlist = ["name", "idiot",
            "qwertyuiopasdfghjklzxcvbnmxcvbnmmm", "totalitarianism", "wow"]

stats = {'a': 0.1667, 'b': 0.0556, 'c': 0.0, 'd': 0.0556, 'e': 0.0, 'f': 0.0, 'g': 0.0, 'h': 0.0, 'i': 0.1111, 'j': 0.0, 'k': 0.0, 'l': 0.0,
         'm': 0.2222, 'n': 0.2222, 'o': 0.1111, 'p': 0.0, 'q': 0.0, 'r': 0.0, 's': 0.0, 't': 0.0556, 'u': 0.0, 'v': 0.0, 'w': 0.0, 'x': 0.0, 'y': 0.0, 'z': 0.0}

scoreTotal = []


def getWordScore():
    for w in wordlist:
        for c in w:
            scoreTotal[w] = scoreTotal[w] + stats[c]


# getWordScore()
# print(scoreTotal)

#x = 'abomination'
#total = 0
#     # for i in removeDuplicates(x):
#    total = total + stats[i]
# print(total)

def makeScoreFile():
    with open("scoreFile.txt", "r+") as f:
        d = f.readlines()
        f.seek(0)
        for line in d:
            total = 0
            for c in removeDuplicates(line):
                total = total + stats[c]
                line = line + str(total)


makeScoreFile()


# def getScoreFile():
#     scoreList = []
#     with open(scoreFile.txt):
#         for line in fin:
#             scoreList.append(line)
#     scoreDict = {}
#     for w in wordlist:
#         total = 0
#         for c in removeDuplicates(w):
#             total = total + stats[c]
#         scoreDict[w] = total


# getScoreDict()
# print(scoreDict.items())
