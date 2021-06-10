from collections import Counter
from typing import List

with open("day04.txt", "r") as file:
    spreadsheet = []
    spreadsheet = [[item for item in line.split()] for line in file]

print("an example passphrase")
print(spreadsheet[0])


def isvalidpassphrase(passphrase: List[str]) -> bool:
    return len(passphrase) == len(set(passphrase))


assert isvalidpassphrase("aa bb cc dd ee".split())
assert isvalidpassphrase("aa bb cc dd ee aa".split()) == False
assert isvalidpassphrase("aa bb cc dd ee aaa".split()) == True

number_valid = 0
for passphrase in spreadsheet:
    if isvalidpassphrase(passphrase):
        number_valid += 1

print(
    f"The number of valid passphrases is {number_valid} of {len(spreadsheet)} candidates "
)


def isvalidpassphrase_anagram(passphrase: List[str]) -> bool:
    uni_phrases = len(set("".join(sorted(phrase)) for phrase in passphrase))
    # print(len(passphrase), uni_phrases)
    return len(passphrase) == uni_phrases


assert isvalidpassphrase_anagram("abcde fghij".split()) == True

assert isvalidpassphrase_anagram("abcde xyz ecdab".split()) == False

assert isvalidpassphrase_anagram("iiii oiii ooii oooi oooo".split()) == True

assert isvalidpassphrase_anagram("oiii ioii iioi iiio".split()) == False

number_valid_anagrams = len(
    [1 for phrase in spreadsheet if isvalidpassphrase_anagram(phrase)]
)

print(
    f"The number of valid passphrases that are not anagrams is {number_valid_anagrams}"
)
