st = input("enter the string")
def count(st):
    di = {}
    for letter in st:
        if letter not in di:
            di[letter] = 1
        else:
            di[letter]+=1
    for key,value in di.items():
        print(f"{key} ==> {value}")
