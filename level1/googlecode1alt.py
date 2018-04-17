from math import sqrt



def answer(area):
    temp_a = area
    l = []
    while(temp_a != 0):
        if(sqrt(temp_a).is_integer()):
            l.append(temp_a)
            area = area - temp_a
            temp_a = area
        else:
            temp_a = temp_a -1
    return l 
l = answer(12)
print(l)


