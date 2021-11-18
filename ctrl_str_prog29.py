count=0
sum=0
number=1

while number!=0:
    number=int(input("ENter number: "))
    sum=sum+number
    count+=1
    mean=sum/count

if count==0:
    print()
else:
    print(f"RESULT: Quantity={count}, Sum={sum}, Mean={mean}")