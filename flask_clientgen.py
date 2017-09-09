import random
import sys
from flask import Flask

app = Flask(__name__)

#Putting the .txt lists into a python list of strings and then defining
#functions to pull a single element

files = open("adject.txt") 
adjectives = files.read()
adjectives = adjectives.splitlines()
files.close()
def pickadjective():
    return adjectives[random.randint(0,len(adjectives)-1)].capitalize()

files = open("nouns.txt") 
nouns = files.read()
nouns = nouns.splitlines()
files.close()
def picknoun():
    return nouns[random.randint(0,len(nouns)-1)].strip().capitalize()

files = open("names.txt")
names = files.read()
names = names.splitlines()
files.close()
def pickname():
    return names[random.randint(0,len(names)-1)].rstrip()

files = open("places.txt")
places = files.read()
places = places.splitlines()
files.close()
def pickplace():
    return places[random.randint(0,len(places)-1)]

files = open("trades.txt")
trades = files.read()
trades = trades.splitlines()
files.close()
def picktrade():
    return trades[random.randint(0,len(trades)-1)].rstrip()

files = open("verbs.txt")
verbs = files.read()
verbs = verbs.splitlines()
files.close()
def pickverb():
    return verbs[random.randint(0,len(verbs)-1)]

def generate(i=1):
    html = ""
    while i > 0:
        options = random.randint(1,8)
        if options == 1: #verbify, only if the verb doesn't end in a/e/i/o/u/y
            endvowels = 1
            currentverb = ""
            vowels = "aeiouy"
            while endvowels > 0:
                currentverb = pickverb()
                if any(vowel in currentverb[len(currentverb)-1] for vowel in vowels):
                    endvowels = 1
                else:
                    endvowels = 0
            html = html + (currentverb.capitalize() + "ify" + "<br>")
            endvowels = 1
            i -= 1
        elif options == 2: #verbtsy, only if the verb ends in t
            endt = 1
            currentverb = ""
            while endt > 0:
                currentverb = pickverb()
                if currentverb[len(currentverb)-1] == "t":
                    endt = 0
            html = html + (currentverb.capitalize() + "sy" + "<br>")
            endt = 1
            i -= 1
        elif options == 3: #nounster, only if the noun doesn't end in s/er
            ends = 1
            currentnoun = ""
            while ends > 0:
                currentnoun = picknoun()
                if currentnoun[len(currentnoun)-1] != "s" and currentnoun[len(currentnoun)-2:len(currentnoun)-1] != "er":
                    ends = 0
            html = html + (currentnoun + "ster" + "<br>")
            ends = 0
            i -= 1
        elif options == 4: #location objects (, objects (and objects))
            currentplace = pickplace()
            currentnoun = picknoun()
            extension = ""
            extensionmid = ""
            ext = random.randint(0,2)
            if currentnoun[len(currentnoun)-1] != "s" and currentnoun[len(currentnoun)-1] != "y":
                currentnoun = currentnoun + "s"
            if ext == 1:
                extension = picknoun()
                if extension[len(extension)-1] != "s" and extension[len(extension)-1] != "y":
                    extension = extension + "s"
                extension = " and " + extension
            elif ext == 2:
                extensionmid = picknoun()
                if extensionmid[len(extensionmid)-1] != "s" and extensionmid[len(extensionmid)-1] != "y":
                    extensionmid = extensionmid + "s"
                extensionmid = ", " + extensionmid
                extension = picknoun()
                if extension[len(extension)-1] != "s" and extension[len(extension)-1] != "y":
                    extension = extension + "s"
                extension = extensionmid + " and " + extension
            html = html + (currentplace + " " + currentnoun + extension + "<br>")
            i -= 1
        elif options == 5: #person's objects (, objects (and objects))
            currentname = pickname()
            currentnoun = picknoun()
            extension = ""
            extensionmid = ""
            ext = random.randint(0,2)
            if currentnoun[len(currentnoun)-1] != "s" and currentnoun[len(currentnoun)-1] != "y":
                currentnoun = currentnoun + "s"
            if ext == 1:
                extension = picknoun()
                if extension[len(extension)-1] != "s" and extension[len(extension)-1] != "y":
                    extension = extension + "s"
                extension = " and " + extension
            elif ext == 2:
                extensionmid = picknoun()
                if extensionmid[len(extensionmid)-1] != "s" and extensionmid[len(extensionmid)-1] != "y":
                    extensionmid = extensionmid + "s"
                extensionmid = ", " + extensionmid
                extension = picknoun()
                if extension[len(extension)-1] != "s" and extension[len(extension)-1] != "y":
                    extension = extension + "s"
                extension = extensionmid + " and " + extension
            html = html + (currentname + "'s " + currentnoun + extension + "<br>")
            i -= 1
        elif options == 6: #location trades
            currentplace = pickplace()
            currenttrade = picktrade()
            html = html + (currentplace + " " + currenttrade + "s" + "<br>")
            i -= 1
        elif options == 7: #person and co trades
            currentname = pickname()
            currenttrade = picktrade()
            company = random.randint(0,4)
            if company == 0:
                currentname = currentname + " and Co. "
            elif company == 1:
                currentname = currentname + " and Family "
            elif company == 2:
                currentname = currentname + " and Daughters "
            elif company == 3:
                currentname = currentname + " and Sons "
            elif company == 4:
                currentname = currentname + " and Friends "
            html = html + (currentname + currenttrade + "s" + "<br>")
            i -= 1
        elif options == 8: #meaningless compound words
            html = html + (picknoun() + picknoun() + "<br>")
            i -= 1
        elif options == 9: #perons's adjective nouns
            currentname = pickname()
            currentnoun = picknoun()
            currentadj = pickadjective()
            extension = ""
            extensionmid = ""
            ext = random.randint(0,2)
            if currentnoun[len(currentnoun)-1] != "s" and currentnoun[len(currentnoun)-1] != "y":
                currentnoun = currentnoun + "s"
            if ext == 1:
                extension = picknoun()
                if extension[len(extension)-1] != "s" and extension[len(extension)-1] != "y":
                    extension = extension + "s"
                extension = " and " + extension
            elif ext == 2:
                extensionmid = picknoun()
                if extensionmid[len(extensionmid)-1] != "s" and extensionmid[len(extensionmid)-1] != "y":
                    extensionmid = extensionmid + "s"
                extensionmid = ", " + extensionmid
                extension = picknoun()
                if extension[len(extension)-1] != "s" and extension[len(extension)-1] != "y":
                    extension = extension + "s"
                extension = extensionmid + " and " + extension
            html = html + (currentname + "'s " + currentadj + " " + currentnoun + extension + "<br>")
            i -= 1
    return html

@app.route('/<number>')
def homepage(number):
    html = """<!DOCTYPE html>
    <head>
      <title>Company namer</title>
      <style>
      body{
      text-align: center;
      }
      </style>
    </head>
    <body>
      <h1>Company namer</h1>
      <p> Refresh to generate a new list. </p>
      <p> Replace the number at the end of the URL to change how many are generated </p>
    """
    html = html + generate(int(number)) + "</body>"
    return(html)

if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)
