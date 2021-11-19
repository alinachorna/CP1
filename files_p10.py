file = open('me.txt','w')
me=['Alina Chorna','UEK w Krakowie','Informatyka Stosowana']
for i in me:
    file.write(i+'\n')
    #file.write("\n")
file.close()

file = open('me.txt','r')

content=file.read()
print(content)

file.close()


