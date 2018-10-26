#Kaitlyn Zhen

import random

def build_random_list(num_items,max_value):
    l = []
    for i in range(num_items):
        l = l + [ random.randrange(0,max_value)]
    return l


def max(l):
    largest_i = 0
    for i in range(1,len(l)):
        if l[i] > l[largest_i]:
            largest_i = i
    return largest_i
    
p = build_random_list(10, 100)
largest_index = max(p)
print("Test for max")
print(p)
print("Index is " + str(largest_index) + ", " + "Largest value is " + str(p[largest_index]))



def freq(l,val):
    count = 0
    for value in l:
        if value == val:
            count = count + 1
    return count


k = build_random_list(30,5)
print("Test for freq")
print(k)
print("Frequency of 1 is " + str(freq(k,1)))
print("Frequency of 4 is " + str(freq(k,4)))

    
def mode(l):
    lmode = 0
    for i in range(0,len(l)):
        if freq(l,l[i]) > freq(l,l[lmode]):
            lmode = i
    return l[lmode]

m = build_random_list(30,10)
print("Test for mode")
print(m)
print("Mode is " + str(mode(m)))

        
        
    
    
    
    
    
    
    
    
    
    