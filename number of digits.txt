''' Write a program to count number of digits in a number.
positive test case :
input = 101
output = 3
negative test case :
input = 1.3
output = 1
'''
n = float(input())
i=0
while n> 0:
    n= n//10
    i= 1+i
print(i)



