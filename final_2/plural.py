#Kaitlyn Zhen


def countPlurals(line):
    list = line.split()
    count = 0
    for word in list:
        index = len(word)-1
        if word[index] == "s":
            count = count + 1
    return count
    
    
print(countPlurals("Dogs and cats"))


def notPossessive(line):
    list = line.split()
    count = 0
    for word in list:
        index = len(word)-1
        if word[index] == "s":
            if word[index - 1] != "'":
                count = count + 1
    total = count + countPlurals(line)
    return total

print(notPossessive("Dog's and bunnies and birds"))