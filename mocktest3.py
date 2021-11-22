def f3(n1,n2,n3,n4):
    list=[n1,n2,n3,n4]
    maks=n1
    for num in list:
        if num>maks:
            maks=num
    return maks
f3(5,98,2,69)