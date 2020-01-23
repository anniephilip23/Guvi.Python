a = float(input())
b = round(a,0)
if b >= 0:
    x = a % 2
    if x == 0:
        print("Even")
    else:
        print("Odd")
elif a == 0:
    print("Zero")

