def piglatinify(word):
    first_letter = word[:1]
    rest_word = word[1:]
    
    if first_letter in "aeiou":
        print(word + "ay")
        
    else:
        print(rest_word + first_letter + "ay")
        
piglatinify("apple")
piglatinify("banana")
piglatinify("elephant")
piglatinify("ink")
piglatinify("movie")