def letter(c):
    count=0
    #c='e'
    txt="You never get a second chance to make a first impression."
    for pos,char in enumerate(txt): #enumerate takes character and position
        if (char==c):
            count+=1
    print(count)

letter("e")


