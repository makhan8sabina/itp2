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