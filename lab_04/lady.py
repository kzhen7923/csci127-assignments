def happyLadybugs(length,l):
    bucket = {}
    for value in list(l):
         if value != "_":
             bucket[value] = 0
    for value in list(l):
        if value != "_":
            bucket[value] = bucket[value] + 1
    if 1 not in bucket.values():
        return "YES"
    else:
        return "NO"
                 


b1_length = 7
b1 = "RRBG_GB"

b2_length = 4
b2 = "BYB_"

b3_length = 3
b3 = "O_O"

b4_length = 8
b4 = "RBY_RBPP"

print(happyLadybugs(b1_length,b1))
print(happyLadybugs(b2_length,b2))
print(happyLadybugs(b3_length,b3))
print(happyLadybugs(b4_length,b4))



