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