print("Enter words until the condition reached")
word_store={}
for m in range(1,21):
    j=input()
    k=len(j)
    word_store.update({m:k})
print(word_store)
