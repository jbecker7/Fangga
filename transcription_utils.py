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

    # Convert the entire word to lowercase first for consistency
    word = word.lower()

    # Handle special characters and combinations next
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
    word = word.replace("c", "q")

    # Directly replace 'ng' with 'NG' to handle it as a single unit
    word = word.replace("ng", "NG")

    return word


def romanizationToManchu(romanization):
    """Converts romanization to Manchu letters"""
    preprocessed_word = preprocessManchuWord(romanization)
    dictmanchuletter = loadManchuDict()
    manjuword = ""
    i = 0
    while i < len(preprocessed_word):
        if i < len(preprocessed_word) - 1 and preprocessed_word[i : i + 2] == "NG":
            # ng is really annoying lmao this works finally
            manjuword += dictmanchuletter["NG"]
            i += 2  # Skip the next character as 'NG' is already processed
        elif preprocessed_word[i] in dictmanchuletter:
            manjuword += dictmanchuletter[preprocessed_word[i]]
            i += 1
        else:
            manjuword += preprocessed_word[i]
            i += 1
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
