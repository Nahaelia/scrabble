
ScrabbleDic = open('Redirecting.txt', 'r')
WORDS = [line.split('\n')[0] for line in ScrabbleDic.readlines()]

import itertools


def checkWord(word, WORDS):
    if word in WORDS:
        return True



def scrabble(available_letters):
    solutions = []
    for i in range(0,len(available_letters)+1):
        available_letters = available_letters.upper()
        for subset in itertools.combinations(available_letters, i):
            permus = list(itertools.permutations(subset))
            for p in permus:
                sp = ''.join(p)
                res = checkWord(sp,WORDS)
                if res is True and sp not in solutions:
                    solutions.append(sp)
    return solutions
