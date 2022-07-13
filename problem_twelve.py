numilist1=[]
numlist2=[]
n=int(input("entr the number of element:"))
for a in range(n):
    m=input("enter the element{}:".format(a+1))
    numilist1.append(m)
print(numilist1)
l=int(input("enter the number of element of list2:"))
for k in range(l):
    j=input("enter element{}:".format(k+1))
    numlist2.append(j)
print(numlist2)
difference=set(numilist1).difference(numlist2)
print("the difference are:",difference)


