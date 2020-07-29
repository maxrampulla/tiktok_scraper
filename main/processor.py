import csv
import numpy as np
import nltk
import os
import nltk.corpus
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import numpy as np


# takes a csv full of strings and tokenizes the files
def tokenizer(csv):
    text = ""

    # read csv into a string
    with open(csv, "r") as file:
        for row in file:
            text = text.replace("\n", "") + row + " "

    # tokenize string and turns everything into lowercase
    token = word_tokenize(text)
    lowerToken = [i.lower() for i in token]

    # filter out non-alphanumeric
    filToken = [i for i in lowerToken if i.isalnum()]

    # lemmatizaton
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    lemToken = [lemmatizer.lemmatize(i) for i in filToken]

    # filter out English stopwords
    from nltk.corpus import stopwords
    a = set(stopwords.words("english"))

    finalToken = [x for x in lemToken if x not in a]

    # filters out other bs
    a = ["fyp", "foryou", "foryoupage", "duet", "wa", "xyzbca", "reply",
         "like", "get", "tiktok","tiktoktaughtme", "know", "vibezone", "fypシ",
         "make", "video", "got", "u", "dc", "fy", "new", "let", "na", "2","go",
         "see", "think", "really", "back", "said", "ha", "first",
         "foryourpage"]
    finalToken = [x for x in finalToken if x not in a]

    return finalToken


# Plots word frequency on a bar chart and then creates a thematic pie chart
def plot(word_list):
    # records the frequency of words
    from nltk.probability import FreqDist
    fdist = FreqDist(word_list)

    values = []  # word
    keys = []   # frequency of word
    for i in fdist.most_common(150):
        values.append(i[1])
        keys.append(i[0])

    plt.bar(range(len(fdist.most_common(150))), values, align='center')
    plt.xticks(range(len(fdist.most_common(150))), keys, rotation=90)
    plt.bar(range(len(fdist.most_common(150))), values, align='center')
    plt.xticks(range(len(fdist.most_common(150))), keys, rotation=90)
    plt.title("TikTok Feed Word Frequency Distribution")
    plt.xlabel("Unique Word Occurence")
    plt.ylabel("Frequency of Word Use out of %s Words Analyzed"
               % len(word_list))
    plt.show()

    # theme distriubtion
    lgbt = ["gay", "lgbt", "lgbtq", "bi", "gayboy", "pride", "nickiminaj",
            "alttiktok", "alt"]
    lgbtqCount = 0
    trend = ["viral", "dance", "privatejet", "legendarychallenge",
             "substepchallenge", "beatsdaisychallenge"]
    techCount = 0
    comedy = ["funny", "comedy", "lol"]
    comedyCount = 0
    politics = ["karen", "trump2020", "quarantine", "politics"]
    politicsCount = 0
    plant = ["plant"]
    plantCount = 0
    utah = ["utah"]
    utahCount = 0
    travel = ["travel"]
    travelCount = 0
    other = 0
    total = 0

    #finds thematic distribution
    for i in fdist.most_common(150):
        if i[0] in lgbt:
            lgbtqCount += i[1]
            total += i[1]
        elif i[0] in comedy:
            comedyCount += i[1]
            total += i[1]
        elif i[0] in politics:
            politicsCount += i[1]
            total += i[1]
        elif i[0] in plant:
            plantCount += i[1]
            total += i[1]
        elif i[0] in utah:
            utahCount += i[1]
            total += i[1]
        elif i[0] in travel:
            travelCount += i[1]
            total += i[1]
        else:
            other += i[1]
            total += i[1]

    # creates a pie chart of distrubtion
    plt.pie([lgbtqCount, comedyCount, politicsCount, plantCount, utahCount,
            travelCount])
    plt.legend(["LGBTQ+ / Alt", "Humor", "Politics & Current Events", "Plants",
                "Utah", "Travel"], loc=8, ncol=3)
    plt.title("Community Distribution TikTok")
    plt.show()

    values = []  # word
    keys = []   # frequency of word
    for i in fdist.most_common(150):
        values.append(i[1])
        keys.append(i[0])
