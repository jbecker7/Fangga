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

    # Handle special characters and combinations first
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
    word = word.replace("š", "x")
    word = word.replace("ū", "v")

    # Process other characters
    new_word = ""
    i = 0
    while i < len(word):
        if i < len(word) - 1 and word[i : i + 2] == "ng":
            # Handle 'ng' as a single unit
            new_word += "NG"
            i += 2
        else:
            if word[i] == "g":
                if i < len(word) - 1 and word[i + 1] not in [
                    "a",
                    "e",
                    "i",
                    "o",
                    "u",
                    "v",
                ]:
                    if i > 0 and word[i - 1] == "n":
                        new_word = new_word[:-1] + "N"  # Replace 'n' with 'N'
                    else:
                        new_word += word[i]
                else:
                    new_word += word[i]
            else:
                new_word += word[i]
            i += 1

    return new_word


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
