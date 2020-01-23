''' Write a program to print multiplication table of any number.
positive test case :
input = 2
output = 2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20
negative test case :
input = 1.3
output = invalid literal for int() with base 10: '1.3'
'''
n = int(input())
for i in range(1,11):
    print(n,"*",i,"=",n*i)



