#Write a program to find the second largest element in an array. Sample result:

list=[5,1,9,6,1]

mx=max(list[0],list[1])
secmx=min(list[0],list[1])
n=len(list)

for i in range (2,n):
    if list[i]>mx:
        secmx=mx
        mx=list[i]
    elif list[i]>secmx and \
        mx != list[i]:
        secmx=list[i]
print(f"Second highest number is : {secmx}")