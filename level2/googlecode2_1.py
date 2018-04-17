def answer(l, t):

    # your code here

    temp = 0

    for x,a in enumerate(l):
        print("------", x)
        temp = a
        print(a,x)
        if l[x] == 12:
            return [x,x]
        for y,b in enumerate(l[x+1:]):
            temp+=b
            print(b,y,temp)
            if temp == t:
                return [x,x+y+1]

    return [-1,-1]

    

print(answer([10], 10))
