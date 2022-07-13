string1=input("enter string:")
dictionery={}
for letter in string1:
    dictionery[letter]=dictionery.get(letter,0)+1
print(dictionery)