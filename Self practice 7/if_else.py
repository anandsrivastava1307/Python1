unit = 210

if unit <=100:
    bill = unit * 3.50
elif unit <= 200:
    bill = unit * 2.50+(unit - 100)*5
else:
    bill = 100 * 3.50 + 100 * 5.00 + (unit - 200) * 7.00


print("Your unit is : ",unit)
print("Your bill is : ",bill)