n = input()
y = len(n)
list = []
for i in range(0,y):
    x = n[i]
    list.append(int(x))
print(list)
list[0],list[y-1] =list[y-1],list[0]
mul =1
for i in list:
    mul =mul* i
print(mul)