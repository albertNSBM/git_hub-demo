list1=[2,3,4,7,8,5,10,9]
f=0
g=0
maximum=list1[0]
for i in list1:
    if i>f:
        f,g=i,f
    elif f>i>g:
        g=i
    if maximum<i:
        maximum=i
print("the run up:",g)
print("the maximu:",maximum)