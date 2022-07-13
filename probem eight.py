l=['g','o','o','g','l','y','m']
dict={}
for i in l:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
print(dict)