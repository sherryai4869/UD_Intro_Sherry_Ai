a = 1
b = 1
c = 1
n = input("please choose a number: ")

for i in range(int(n)):
    d = a+b
    a = b
    b = c
    c = d
    print(a)