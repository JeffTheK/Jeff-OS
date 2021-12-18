from collections import Counter
from .color import colored

def did_you_mean(string: str, dictionary: list):
    rated_words = {}
    for w in dictionary:
        rated_words[w] = sum((Counter(w) & Counter(string)).values())

    rated_words = list(rated_words.items())
    for i, w in enumerate(rated_words):
        len_diff = abs( len(w[0]) - len(string) )
        if len_diff >= 4:
            rated_words.pop(i)

    rated_words = sorted(rated_words, key=lambda x: x[1])
    rated_words.reverse()
    rated_words = rated_words[0:2]
    
    print("did you mean", end="")
    for w in rated_words:
        print(" "+colored(w[0], "cyan"), end="")
    print("?")