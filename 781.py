n = int(input())
list = []
for i in range(1,n+1):
    if n == 0:
        print("NULL")
    elif n > 0:
        a = 9 * i
    list.append(a)

print(*list, sep = " ")


