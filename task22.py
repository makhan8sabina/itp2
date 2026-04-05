amount=int(input("Enter amount:"))
distance=int(input("Enter distance:"))

if amount>1500:
    print("Free delivery")
elif distance>5:
    print("Total:", (distance-5)*200+1000)
else:
    print('Total:', 1000+amount)
