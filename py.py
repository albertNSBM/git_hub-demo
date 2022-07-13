j=input('enter string:')
dictionary={}
for i in j:
    dictionary[i]=dictionary.get(i,0)+1
print(dictionary)
