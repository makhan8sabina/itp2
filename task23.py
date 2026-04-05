salary=float(input("Enter your salary:"))
history=input("Enter your credit history:")

if salary>=200000 and history=='good':
    print("Approved")
else:
    print("Rejected")