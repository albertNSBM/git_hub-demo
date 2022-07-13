

words = input("enter word:")
dictionary = {}
for i in range(1,21) :
    if (i[0] not in dictionary.keys()):

        dictionary[word[0]] = []
        dictionary[word[0]].append(word)


    else:
        if (word not in dictionary[word[0]]):
            dictionary[word[0]].append(word)


print(dictionary)