def answer(s):

    # your code here

    num_salutes = 0

    for a,c in enumerate(s):
        if c == '>':
            for b,d in enumerate(s[a:]):
                if d == '<':
                    num_salutes += 2
            
    return num_salutes  

print(answer('<>>--<'))
