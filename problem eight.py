list1 = []
num = [x for x in input().split(',')]
for i in num:
    x = int(i,2)
    if not x % 5:
        list1.append(i)
print(','.join(list1))
