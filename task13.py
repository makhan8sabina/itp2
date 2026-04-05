#TASK13
amount=int(input())
if amount==1000:
    print(amount-(amount/100*10))
elif amount==500:
    print(amount-(amount/100*5))
else:
    print('No discount')