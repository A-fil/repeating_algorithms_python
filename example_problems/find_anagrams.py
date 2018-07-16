from typing import List, Dict
from random import shuffle

# Stores anagrams in a Hash Table

anagram1 = ["abets", "baste", "betas", "beast", "beats"]
anagram2 = ["angel", "angle", "glean"]
anagram3 = ["drawer", "redraw", "reward", "warder", "warred"]

words = anagram1 + anagram2 + anagram3
shuffle(words)


def find_anagram(words: List[str]) -> List[List[str]]:
    word_groups = {}  # Empty hash table
    for word in words:
        key = ''.join(sorted(word))
        word_groups.setdefault(key, []).append(word)

    anagrams = []
    for key, value in word_groups.items():
        anagrams.append(value)

    return anagrams


print("Anagram 1: {}".format(anagram1))
print("Anagram 2: {}".format(anagram2))
print("Anagram 3: {}".format(anagram3))

results = find_anagram(words)
print("Result 1: {}".format(results[0]))
print("Result 2: {}".format(results[1]))
print("Result 3: {}".format(results[2]))
