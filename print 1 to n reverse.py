'''Write a program to print all natural numbers in reverse (from n to 1). - using while loop
positive test case :
input = 10
output = 10 9 8 7 6 5 4 3 2 1
negative test case :
input = -2
output = exit program
'''
n = int(input())
list =[]
i = n
while i >= 1 :
    list.append(i)
    i=i-1
print(*list, sep =" ")
