def check(x,y,num):
    is_in=False
    #num=5
    if num>=x and num<=y:
        is_in=True
    return is_in
print(check(1,10,12))
