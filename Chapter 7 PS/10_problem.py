#Questioon 10 : Write a program to print multiplication table if n using for loops in reversed order.
# Method 1 — Pehla wala (thoda tricky)
for i in range(1, 11):
    print(f"{n} X {11 - i} = {n*(11-i)}")

# Method 2 — Ye wala (clean & simple ✅)
for i in range(10, 0, -1):
    print(f"{n} X {i} = {n*i}")