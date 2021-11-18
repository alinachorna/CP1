
num=int(input("Enter the amount in PLN: "))

in_num=num
am5=num//5
#am2=(num-am5)//2
#am1=num-am5-am2

if am5!=0: 
    num=num-5*am5
    am2=num//2
    am1=num%2
    

elif num//2!=0:
    am5=0
    am2=num//2
    am1=num%2

print(f"The amount of PLN {in_num} in coins: ")
print(f"5 zł - {am5}")
print(f"2 zł - {am2}")
print(f"1 zł - {am1}") 