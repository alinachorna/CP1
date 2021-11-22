#W pierwszych pięciu latach pracy pracownik otrzymuje dodatek stażowy w wysokości 100 zł za każdy przepracowany rok
#a w kolejnych trzech latach 200 zł za każdy przepracowany rok.  W pozostałych latach dodatek wynosi 50 zł za każdy przepracowany rok. 
# Zdefiniuj funkcję f6(n), która dla podanych lat pracy nzwróci wielkość dodatku stażowego. 

def f6(n):
    if n<=5:
        dod=n*100
    elif n>5 and n<=8:
        dod=5*100+(n-5)*200
    elif n>8:
        dod=5*100+3*200+(n-8)*50
    
    return dod
#print(f6(7))
f6(9)


