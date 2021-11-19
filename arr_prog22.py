arr=[5,1,9,6,1]
a=min(arr)
b=max(arr)
diff=b-a

print ('Array: ', end='')
for i in arr:
    print (i, end=' ')
print()

print(f'Result: {diff}')
