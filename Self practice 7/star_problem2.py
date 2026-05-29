'''*
**
***
****
***** '''

n = int(input("Enter your number : "))

for i in range(1, n+1):        # ← Outer loop (row)
    for n in range(i):       # ← INNER LOOP ✅
        print("*", end="")   # ← INNER LOOP ka kaam ✅
    print()                  # ← Outer loop ka kaam