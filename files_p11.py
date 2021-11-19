film_titles=['Once Upon a Time in Hollywood','Call Me By Your Name','Spirited Away','Love Actually','The Grand Budapest Hotel']
file = open('movie.txt','w')
for film in film_titles:
    file.write(film+"\n")

file.close()

file = open('movie.txt','r')
content=file.read()
print(content)
file.close()
