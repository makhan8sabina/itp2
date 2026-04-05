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