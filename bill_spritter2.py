import random
a=int(input('enter the number of friends to come in patty:\n'))
if a>0:
    print("enter the friends:")
    frienddictionary={}
    for n in range(1,a+1):
        c=input()
        frienddictionary.update({c:0})
    print('enter the bill value:')
    bill=int(input())
    list1 = list(frienddictionary.keys())
    total_bill=bill/a
    for n in list1:
        frienddictionary.update({n:round(float(total_bill),2)})
    print('doyou want to use the lack one??')
    choice=input()
    if choice=='YES'or choice=='yes':
        choosenone = random.choice(list1)
        print('{} is the luck one'.format(choosenone))

        for n in list1:
            if n==choosenone:
                frienddictionary.update({n:0})
            else:
                total_bill = bill / (a - 1)
                frienddictionary.update({n: round(float(total_bill), 2)})
        print(frienddictionary)
    else:
        print('none is going to be luck')
        print(frienddictionary)


else:
    print('none joing the party')