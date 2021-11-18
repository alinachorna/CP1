human=int(input("Enter the dog's age in human years: "))

dog=0
if human<=2:
    dog=human*10.5
else:
    dog=2*10.5+(human-2)*4

print(f"The dog's age in dog’s years is {int(dog)} years.")