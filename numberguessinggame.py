import random
a = random.randrange(10)
i = 5
while (i!=0):
    n = int(input("enter any number between 0 to 10: "))
    if a==n:
        print ("u have entered correct number")
        break
    else:
        print ("enter any other numb. Your life left is ",i-1)
    i=i-1
print ("gameover the number is",a)

