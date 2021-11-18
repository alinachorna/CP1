side_a=int(input('a:'))
side_b=int(input('b:'))
side_c=int(input('c'))
#semi-perimeter:

sem=(side_a+side_b+side_c)/2

area=(sem*(sem-side_a)(sem-side_b)(sem-side_c))*(1/2)
print("Area of triangle is equal to:"+area)