a=input('enter the string:')
count1=0
upper2=0
for n in a:
    if n ==n.upper():
        upper2=upper2+1
    if n ==n.lower():
        count1= count1 + 1
print('lower:',count1)
print('upper:',upper2)