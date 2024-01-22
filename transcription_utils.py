import aqt
import json
import os


def loadManchuDict():
    """Imports the dictionary of romanization to Manchu letters"""
    addons_path = aqt.mw.addonManager.addonsFolder()
    json_path = os.path.join(addons_path, "Fangga", "manchudict.json")
    with open(json_path, "r", encoding="utf-8") as file:
        return json.load(file)


def preprocessManchuWord(word):
    """Fixes romanization of Manchu words to match the dictionary"""

    word = word.replace("k'", "K")
    word = word.replace("g'", "G")
    word = word.replace("h'", "H")
    word = word.replace("ts'", "T")
    word = word.replace("dz", "D")
    word = word.replace("z", "Z")
    word = word.replace("sy", "S")
    word = word.replace("c'y", "C")
    word = word.replace("jy", "J")
    word = word.replace("ts", "Q")

    vowel = ["a", "e", "i", "o", "u", "v"]
    i = 0
    while i < len(word):
        if word[i] == "g":  ##case of "ng+consonant" or final "ng".
            if i < len(word) - 1:  ##not final "g"
                if (
                    word[i + 1] not in vowel and word[i - 1] == "n"
                ):  # letter "g" in "ng+consonant" case
                    word = word[: i - 1] + "N" + word[i + 1 :]
            elif (
                i == len(word) - 1 and word[i - 1] == "n"
            ):  ##final "g", i.e. "ng" at the final part of a word.
                word = word[: i - 1] + "N"
        i += 1

    return word


def romanizationToManchu(romanization):
    """Converts romanization to Manchu letters"""
    preprocessed_word = preprocessManchuWord(romanization)
    dictmanchuletter = loadManchuDict()
    manjuword = ""
    for letter in preprocessed_word:
        if letter in dictmanchuletter:
            manjuword += dictmanchuletter[letter]
        else:
            manjuword += letter
    return manjuword


def manchuToRomanizationDict():
    """Creates a dictionary of Manchu letters to their romanization"""
    """I could prob just make another json lol"""
    dictmanchuletter = loadManchuDict()
    return {v: k for k, v in dictmanchuletter.items()}


def manchuToRomanization(manchuword):
    """Converts Manchu letters to romanization"""
    dictlatinletter = manchuToRomanizationDict()
    latinword = ""
    for character in manchuword:
        if character in dictlatinletter:
            latinword += dictlatinletter[character]
        else:
            latinword += character
    return latinword
