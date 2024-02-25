import string
import random


cod = int(input("Enter 0 for coding and 1 for decoding: "))
text = input("Enter a text: ")

text = text.split(' ')
textlist = list(text)

codedlist = []
decodedlist = []


if cod == 0:
   for i in range(len(textlist)):
    word = textlist[i]
    for i in range(3):
       randletter = random.choice(string.ascii_lowercase)
       word =  randletter+word[::-1]+word[:1]+randletter
    codedlist.append(word)
    codedlist.append(' ')

elif cod == 1:
    for i in range(len(textlist)):
        word = textlist[i]
        nstring = word[4:-4]
        a = nstring[:-1]
        b = a[::-1]
        decodedlist.append(b)
        decodedlist.append(' ')

codedtext = ""
decodedtext = ""

for i in codedlist:
   codedtext += i

for i in decodedlist:
   decodedtext += i

print(codedtext)
print(decodedtext)
