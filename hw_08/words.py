def list_comp(l):
    d = {}
    list = l.split()
    for word in list:
        if word not in d.keys():
            d.setdefault(word,[])
    for i in range(0,len(list)-1):
        if list[i] in d.keys():
            d[list[i]].append(list[i+1])
    return d

f = open("/home/kz87/Test/macbeth.txt")
s = f.read()

print(s)
print(list_comp(s))