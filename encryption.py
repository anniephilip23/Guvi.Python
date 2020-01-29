lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
             'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
             't', 'u', 'v', 'w', 'x', 'y', 'z']
def enct(letter):
    a = []
    for element in letter:
        if element in lowercase:
            index = lowercase.index(element)
            step =5
            crypt = (index + int(step))%26
            newletter= lowercase[crypt]
            a.append(newletter)
    listToStr = "".join(map(str,a))
    print("the encrypted letter is",listToStr)

enct(input("enter the letters:"))



