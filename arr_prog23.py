def median(lst):
    n = len(lst)
    s = sorted(lst)
    return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2] if n else None

arr1=[1,0,9,4,6]
arr2=[6,8,3,1,0,5,7]
print(median(arr1))
print(median(arr2))
#import statistics as s
