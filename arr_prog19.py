arr=[2,3,2,5,8,1,9,8]

unique=[]

for i in arr:
    if i not in unique:
        unique.append(i)
print("Array",end=' ')
for i in arr:
    print(i,end=' ')

print()
print("Unique elements:",end=' ')
for x in unique:
    print(x,end=' ')
    