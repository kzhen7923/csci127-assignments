def happyLadybugs(length,list):
    colors = []
    pairs = []
    for value in list:
         if value != "_":
             if value not in colors:
                 colors.append(value)
                 pairs.append(1)
             else:
                 pairs[colors.index(value)] += 1
    if 1 not in pairs:
        return "YES"
    else:
        return "NO"
                 


b1_length = 7
b1 = "RRBG_GB"

b2_length = 5
b2 = "BYB__"

b3_length = 3
b3 = "O_O"

b4_length = 8
b4 = "RBY_R"

print(happyLadybugs(b1_length,b1))
print(happyLadybugs(b2_length,b2))
print(happyLadybugs(b3_length,b3))
print(happyLadybugs(b4_length,b4))



