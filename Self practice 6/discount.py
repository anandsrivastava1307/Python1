amount = int(input("Enter your amount : "))

if(amount>1000):
    discount = amount * 0.10
    final_bill = amount - discount
    print("Your final bill after 10% discount : ", final_bill)

else:
    final_bill = amount
    print("Your final bill : ",final_bill)