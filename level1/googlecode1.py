from math import sqrt



def answer(area):
    temp_a = area
   
    while(temp_a != 0):
        if(sqrt(temp_a).is_integer()):
            if(area == 1):
                return 1
            else:
                l = [temp_a]
                s = [answer(area-temp_a)]
                l = l + s
                return l 
        else:
            temp_a = temp_a - 1

l = answer(12)
print(l)
