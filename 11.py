myList = []
for i in range(20):
    myList.append(i*5)
print(myList)


def wonderwhy(n):
    div = 0
    for i in range(1,int(n/2)+1):
        if n%i==0:
            div = i
            print(i)
    return div
wonderwhy(20)

Dictionary = {
    'flower':'blue',
    'sofa':'brown',
    'vase':'white',
    'bowl':'grey',
    'lemon':'yellow',
    'me':'dream'}

def WWse(d,k):
    for t in d.keys():
        if k == t:
            return True
    return False
WWse (Dictionary, 'me')