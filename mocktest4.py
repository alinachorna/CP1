def f4(n):
    am5=n//5
    am2=0
    am1=0
    if n==1:
        am1=1
    elif am5!=0:
        if n%5!=0:
            am2=(n-(am5*5))//2
            if am2!=0:
                if(n-(am5*5))%2!=0:
                    am1=n-am2*2-am5*5
            elif am2==0:
                am1=n-am2*2-am5*5
 
    elif am5==0:
        am2=n//2
        if am2!=0:
            if n%2!=0:
                am1=n%2
    liczba=am5+am2+am1
    return(liczba)

f4(23458)

#print(f4(23458))