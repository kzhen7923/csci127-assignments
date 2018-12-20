#Kaitlyn Zhen

def addline(d,line):
    list = line.split()
    for word in list:
        word = word.lower()
        if word[0] in d.keys():
            letter = word[0]
            d[letter].append(word)# did not know how to append new values to keys
        else:
            d[word[0]] = word
    return d

p = {}
print(addline(p,"What a nice day"))
print(addline(p, "Today's wonderful"))




def spellCheck(d,word):
    word = word.lower()
    if word in d.values():
        return True
    else:
        return False
    
            
print(spellCheck(p,"All"))
print(spellCheck(p, "DAY"))
print(spellCheck(p, "WHAT"))



