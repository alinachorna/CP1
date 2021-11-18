num = 1
#flag=False

while num!=0:
    num = int(input("Enter a number: "))
    for i in range(2,num):
        if(num%i)==0:
           # flag=True
            break
    else:
        print(num,end='')
    