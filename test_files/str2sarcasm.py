"""
Takes your clipboard and converts the text to sarcasm

clipboard: "Im having too much fun at this..."
result: "iM hAvInG tOo MuCh FuN aT tHiS..."

"""

import pyperclip

text = str(pyperclip.paste())
sarc = ""

c = 0
for n in text:
    c+=1
    #ignoring spaces
    if n != " ":
        #modulus operator or something, used for every other letter
        if c%2==0:
            sarc += n.capitalize()
        else:
            sarc += n.lower()
    else:
        sarc += " "
        c+=1

#join list and copy to clipboard
pyperclip.copy(sarc)
