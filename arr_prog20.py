def occurs(number, array):
    if number in array:
        return True
    else:
        return False
    
array=[15, 38, 7, 23, 14]
number=int(input("Number:"))
print(f"Number: {number}")
print(f"Array: {array}")

#occurs(number, array)
if occurs(number, array)==True:
    print(f"Result: number {number} appears in the array")
else:
    print(f"Result: number {number} not in the array")
