score=int(input("Enter score:"))
attendance=int(input("Enter attendance:"))

if score<=49:
    print('Fail')
elif 50<=score<=74:
    print('C')
elif 75<=score<=89:
    print('B')
elif 90<=score<=100:
    print('A')

if attendance<=60:
    print('Fail')