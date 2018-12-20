#Kaitlyn Zhen

def canMakeWord(letters,word):

    word_list = list(word)
    new_list = []

    for char in word_list:
        if char in letters:
            new_list.append(char)
        else:
            return False
    print(new_list)
    return True
    
    

def withWild(letters,word):
    word_list = list(word)
    letter_list = list(letters)
    new_list = []
    wild_count = 0
    missing_count = 0
    for char in word_list:
        if char in letters:
            new_list.append(char)
        else:
            missing_count += 1
            
    for value in letter_list:
        if value == "?":
            wild_count += 1
            
    if wild_count >= missing_count:
        return True
    else:
        return False
    
    
print(withWild("fon?su???ef", "blue"))
print(withWild("orang?s?", "oranges"))

print(canMakeWord("bafoegppseles","apples"))

print(canMakeWord("eerriin","eerie"))