def power(x,n):
    p=x
    for i in range (n-1):
        p*=x
    print(x,p)
power(5,3)