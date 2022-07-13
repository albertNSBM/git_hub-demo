def withdraw(a,b):
    return a-b
def depositi(a,b):
    return a+b
def balance(a):
    return a

print("1.WITHDWAW")
print("2.DEPOSTIT")
print("1.BALANCE")
print("1.EXIT")
print("please choose in the following:")
currentbalance = 2000000
while True:

    choice=input()
    if choice=="1":
        money=int(input('enter amount:'))
        print('you have withdrown',money,'to',currentbalance,'new balance are',withdraw(currentbalance,money))