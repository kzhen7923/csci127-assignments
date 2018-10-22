def cake(A,B,u):
    slice = A / B
    num_ppl = u / slice
    return int(num_ppl)

print(cake(4,5,3))
print(cake(1,2,1))
print(cake(5,7,2))