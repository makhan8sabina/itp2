#TASK1
name=input()
age=input()
print("Hello "+name+"! " +"You are "+age+" years old.")

#TASK2
a=int(input())
b=int(input())
print("Sum:", a+b)
print("Difference:", a-b)
print("Product:", a*b)

#TASK3
temp=int(input("Celsius temperature:"))
print("Fahrenheit temperature:",temp*9/5+32)

#TASK4
a=5
b=10
print('a =', b)
print('b =', a)


#TASK5
a=int(input())
if a%2==0:
    print('even')
else:
    print('odd')

#TASK6
a=int(input())
if a<=12:
    print('child')
elif a<=17 and a>=13:
    print('teenager')
elif a<=18:
    print('adult')

#TASK7
a=int(input())
b=int(input())
c=int(input())
print(max(a,b,c))

#TASK8
a=int(input())
b=int(input())
c=input()
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='/':
    print(a/b)

#TASK9
a=int(input())
if a%4==0 and a%100!=0 or a%400==0:
    print(a,"is leap year")
else:
    print(a,"is not leap year")

#TASK10
if 0<=a<=49:
    print('F')
elif 50<=a<=74:
    print('C')
elif 75<=a<=89:
    print('B')
elif 90<=a<=100:
    print('A')

#TASK11
#TASK11
a=int(input())
if a<1000:
    print(1000-a)
else:
    print('ERROR')


#TASK12
#TASK12
login = "admin"
password = "1234"
a=input()
b=input()
if a==b:
    print("OK")
else:
    print("Wrong password or login")


#TASK13
#TASK13
amount=int(input())
if amount==1000:
    print(amount-(amount/100*10))
elif amount==500:
    print(amount-(amount/100*5))
else:
    print('No discount')


#TASK14
a=int(input())
b=int(input())
c=int(input())
if a==b and b==c:
    print("equilateral")
elif a==b or b==c or c==a:
    print("isosceles")
elif a!=c and c!=b and b!=a:
    print("scalene")


#TASK15
color=input()
if color=="red":
    print("Stop")
elif color=="green":
    print("Go")
elif color=="yellow":
    print("Wait")


#TASK16
a=int(input())
if a>0:
    print('Positive')
elif a<0:
    print('Negative')
elif a==0:
    print('Zero')
if a%2==0:
    print('Even')
else:
    print('Odd')
if 1<=a<=100:
    print('Yes')
else:
    print('No')


#TASK17
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


#TASK18
password=input()
lenght=len(password)>=8
for a in password:
    if a.isdigit():
        digit=True
    if a.isupper():
        upper=True
if lenght and digit and upper:
    print("Strong")
elif lenght:
    print("Medium")
else:
    print("Weak")


#TASK19
balance=5000

print('1 - Check balance')
print('2 - Deposit')
print('3 - Withdraw')

choice=int(input("Enter choice:"))

if choice==1:
    print('Balance:',balance)
elif choice==2:
    amount=int(input("Enter amount:"))
    print('New balance:', amount+balance)
elif choice==3:
    amount=int(input("Enter amount:"))
    if amount<=balance:
        print('New balance:',balance-amount)
    else:
        print('Not enough money!')
else:
    print('error')



#TASK20
number=7
g=int(input("Enter your number:"))

if g==number:
    print("Correct")
elif g>number:
    print("Too high")
else:
    print("Too low")


#TASK21
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


#TASK22
amount=int(input("Enter amount:"))
distance=int(input("Enter distance:"))

if amount>1500:
    print("Free delivery")
elif distance>5:
    print("Total:", (distance-5)*200+1000)
else:
    print('Total:', 1000+amount)


#TASK23
salary=float(input("Enter your salary:"))
history=input("Enter your credit history:")

if salary>=200000 and history=='good':
    print("Approved")
else:
    print("Rejected")


#TASK24
login=input('Enter your login: ')
password=input('Enter your password: ')

login2=input('Enter your login again: ')
password2=input('Enter your password again: ')

if login==login2 and password==password2:
    print("Login Successful")
else:
    print("Blocked")


#TASK25
print("\nMenu:")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Exit")

a=int(input('Enter a number: '))
b=int(input('Enter another number: '))
c=input()
if c=='Add':
    print(a+b)
elif c=='Subtract':
    print(a-b)
elif c=='Multiply':
    print(a*b)
elif c=='/':
    print(a/b)
elif c=='Exit':
    print("Goodbye")








