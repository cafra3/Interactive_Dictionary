import json
from difflib import get_close_matches
import string

data =json.load(open("data.json")) #dictionary

def definition(word):
    if word in data:
        return data[word]
    elif string.capwords(word) in data:
        return data[string.capwords(word)]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        a = "Did you mean %s?(y/n) " % get_close_matches(word,data.keys())[0]
        answer=input(a)
        if answer == "y":
            return data[get_close_matches(word,data.keys())[0]]
        elif answer =="n":
            return "Not a word, Please double check it."
        else:
            return "We did not understand your entry."
    else:
        return "Not a word"
    # try:
    #     return data[word]
    # except KeyError:
    #     return("Not a word")


w = input("Enter a word: ")

d=definition(w.lower())
if type(d) == list:
    for i in d:
        print(i)
else:
    print(d)
