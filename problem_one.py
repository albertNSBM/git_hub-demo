list1=[]
print("enter the array elment:")
for a in range(5):
    d=int(input())
    list1.append(d)
maximum=list1[0]
minmum=list1[0]
for h in list1:
    if h>maximum:
        maximum=h
    if h<minmum:
        minmum=h
print("minimum:",minmum,"\n maximum are:",maximum)
