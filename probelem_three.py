
a=2000
emputy_list=[]
while a<=3200:
    if a % 7 == 0 and a % 5 !=0:
        emputy_list.append(a)
    a=a+1
print(tuple(emputy_list))