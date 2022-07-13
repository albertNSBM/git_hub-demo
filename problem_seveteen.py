def getfuction(p):
    return 2*p
n=int(input('how many number do you want to enter:'))
all_list=[]
for i in range(n):
    g=int(input('enter the element{}:'.format(i)))
    all_list.append(g)
def check_numbers(x):
    dictionary={}
    list_numduplicate=[]
    for i in x:
        if i not in list_numduplicate:
            list_numduplicate.append(i)
    for i in list_numduplicate:
        dictionary.update({i:getfuction(i)})
    print(dictionary)
check_numbers(all_list)
