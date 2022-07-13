list1=[]
count=0
input("enter the list element:")
for a in range(8):
    g=int(input())
    list1.append(g)
    if a%3==0:
        count=count+1
print("{}in this list are divisible by three".format(count))
