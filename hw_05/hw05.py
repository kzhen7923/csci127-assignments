#Kaitlyn Zhen

def filterodd(l):
    new_list = []
    for i in range(len(l)):
        if l[i] % 2 == 1:
            new_list.append(i)
    return new_list
        
#test for filterodd()
p = [0,1,2,3,4,5,6,7,8,9]
print(filterodd(p))


def mapsquare(l):
    new_list = []
    for i in range(len(l)):
        new_list.append(l[i]**2)
    return new_list

#test for mapsquare()
print(mapsquare(p))
