import json
i = 1
while(i>=1):
    with open("contact.txt") as list:
        name =input("enter the contact name: ")
        y = json.load(list)
        if name in y:
            z= y.get(name)
            print("the contact number is: ",z)
            break
        else:
            print("enter the correct name")
            i=i+1

