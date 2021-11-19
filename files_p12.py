item=input("Enter the item:")
with open("zakupy.txt","a") as file:
    file.write(item+"\n")
    
with open("zakupy.txt","r") as file:
    content=file.read()
print(content)