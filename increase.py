
def order(a,b,c):
    mid = 0
    if a>b and b>c:
        mid = a
        a=b
        b=mid
    elif c<a and c<b:
        mid = a
        a = c
        c = mid
    if c < b:
        mid = b
        b = c
        c = mid
    return (a,b,c)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

x,y,z = order(a,b,c)
print("Original numbers: ", a,b,c)
print("Sorted numbers: ", x,y,z)