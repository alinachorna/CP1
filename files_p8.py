# displaying text file, line by line ...
file = open('countries.txt','r')
num=1
for line in file:
    print(num,line, end="")
    num+=1
file.close()