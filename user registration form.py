''' negative test cases :
case 1:
 Welcome to banking service
press 1 if u want register
press 2 if u want login
Enter your input:2
enter your unique key:1
enter your password:123
Invalid username

case 2:
Welcome to banking service
press 1 if u want register
press 2 if u want login
Enter your input:2
enter your unique key:140
enter your password:
Login Failed

case 3:
Welcome to banking service
press 1 if u want register
press 2 if u want login
Enter your input:3
Welcome to banking service
press 1 if u want register
press 2 if u want login
Enter your input:

Press 1 to withdraw
Press 2 to deposite
Press 3 to exit

Enter your choice: 1
enter the amount u want to withdraw130000
You need to maintain minimum balance of 10000, So withdraw a lesser amount

Positive Testcase :

Welcome to banking service
press 1 if u want register
press 2 if u want login
Enter your input:2
enter your unique key:140
enter your password:123
login successful
your current balance is = 20820
Press 1 to withdraw
Press 2 to deposite
Press 3 to exit

Enter your choice: 2
enter the amount u want to deposite20000
{140: ['ann', 'ann@123', '89076', '123', 40820], 136: ['mick', 'mick@123', '908765', '890', 21288]}
Thank You!

************************************************************************
'''
import random
dictnew ={}
dict ={}
# function to get user details for registration
def form():
    key = []
    name = input("enter your name :")
    key.append(name)
    email = input("enter your email_id :")
    key.append(email)
    ph = input("enter your phone number :")
    key.append(ph)
    pwd = input("enter your pwd : ")
    key.append(pwd)
    balan = random.randrange(15000,25000)
    key.append(balan)
    return key
# function to open text file read for login purpose
def login():
    f = open('form.txt','r')
    c = eval(f.read())
    f.close()
    return c
# function to  withdraw money
def withdraw():
    balance = data[4]
    x = int(input("enter the amount u want to withdraw :"))
    y = balance - x
    if y>10000:
        return y
    else:
        print("You need to maintain minimum balance of 10000, So withdraw a lesser amount")

# function to  deposite  money
def deposite():
    balance = data[4]
    x = int(input("enter the amount u want to deposite"))
    y = balance + x
    return y
# function to choose banking options
def banking():
    balance = data[4]
    print("your current balance is =", balance)
    print("Press 1 to withdraw\n" +"Press 2 to deposite \n"+"Press 3 to exit\n ")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        balance = withdraw()
        return balance
    elif choice == 2:
        balance = deposite()
        return balance
    elif choice == 3:
        balance = balance
        return balance


count = "y"
while (count == "y"):
    a = int(input("Welcome to banking service\n"+"press 1 if u want register\n" + "press 2 if u want login\n"
                  +"Enter your input:"))
    dictnew = {}
    if a == 1:
        b = random.randrange(100,200)
        dict[b] = form()
        print("Your unique ID is : ",b)
        dictnew.update(dict)
        count = input("do u want to continue Y/n:")
        f = open("form.txt", "a+")
        f.write("%s" % dict)
        f.close()

    elif a==2:
        k = int(input("enter your unique key:"))
        pwd1 = input("enter your password:")
        list1 = login()
# reading the data from sheet  and declaring it a variable
# Checking the input key in the dictnory
        if k in list1.keys():
            # set data the value of key
            data = list1.get(k)
            # 3rd position in data is pwd , so chk that with given pwd
            if data[3] == pwd1:
                print("login successful")
                data[4] = banking()
                list1[k]= data
                f = open("form.txt", "w")
                f.write("%s" % list1)
                f.close()
                print("Thank You!")
                count = 'n'

            else:
                print("Login Failed")
        else:
            print("Invalid username")


