d = {"a":1, "e":1, "i":1, "o": 1, "u": 1, "l":1, "n": 1, "r": 1, "s": 1, "t": 1,
     "d":2, "g":2, 'b':3, 'c':3, 'm':3, 'p':3, 'f':4, 'h':4, 'v':4, 'w':4,
     'y':4, 'k':5, 'j':8, 'x': 8, 'q':10, 'z':10}

def score(w):
    l_list = list(w.lower())
    score = 0
    for letter in l_list:
        if letter in d.keys():
            points = d[letter]
            score += points
    return score
        

print(score("Hello"))
print(score("Orange"))
print(score("ZeBraS"))



def encode(string):
    l = list(string)
    whole_list = []
    
    for i in range(len(l)-1):
        sub_list = []
        sub_list.append(l[i])
        count = 0
        for i in range(len(l)-1):
            if l[i] == l[i+1]:
                count += 1
        sub_list.append(count)        
        whole_list.append(sub_list)
        
    return whole_list

print(encode("aaddssaa"))