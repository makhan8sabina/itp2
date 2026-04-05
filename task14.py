a=int(input())
b=int(input())
c=int(input())
if a==b and b==c:
    print("equilateral")
elif a==b or b==c or c==a:
    print("isosceles")
elif a!=c and c!=b and b!=a:
    print("scalene")