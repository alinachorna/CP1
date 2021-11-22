import random


def f5(x,y):
    zm=False
    while zm==False:
        num=random.randint(x,y)
        #print(zm)
        #print(num)
        if num%2==0 and num%3==0:
            zm=True
    return num
#print(f5(1,949))
f5(1,949)

