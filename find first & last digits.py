''' Write a program to find first and last digit of a number
positive test case :
input = 1234
output = 4
         1
negative test case :
input = 1.3
output = error
'''
n = int(input())
print(n%10)
while n>=10:
    n = n/10
print(int(n))




