def makeacronym(w):
    list = w.split()
    new_list = []
    for word in list:
        new_list.append(word[0])
    new_string = "".join(new_list)
    return new_string

print(makeacronym("laugh out loud"))
