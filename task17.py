a=int(input())
b=int(input())
tanba=input()
if tanba=='+':
    print(a+b)
elif tanba=='-':
    print(a-b)
elif tanba=='*':
    print(a*b)
elif tanba=='/':
    if b!=0:
        print(a/b)
    else:
        print('error')
elif tanba=="**":
    print(a**b)
elif tanba=="%":
    print(b*100/a)
else:
    print("error")