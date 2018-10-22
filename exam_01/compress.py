def string(l):
    string = "".join(l)
    return string


def compress_word(w):
    new_word = []
    i = 1
    new_word.append(w[0])
    while i < len(w):
        if w[i] not in ("a","e","i","o","u"):
            new_word.append(w[i])
            i = i + 1
        elif w[i] == "a" or "e" or "i" or "u" or "o":
            i = i + 1
    return string(new_word)

print(compress_word("halloween"))
print(compress_word("oranges"))
print(compress_word("Science"))


def sentence(line):
    new_line = []
    word_list = line.split()
    for item in word_list:
        new_word = compress_word(item)
        new_line.append(new_word)
    string = " ".join(new_line)
    return string

print(sentence("Happy Times"))
print(sentence("I love Monday mornings"))
print(sentence("Knock Knock"))