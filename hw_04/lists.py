#Kaitlyn Zhen

import random

def build_random_list(size,max_value):
    """
    Parameters:
      size : the number of elements in the list
      max_value : the max random value to put in the list
    """
    
    l = []
    
    i = 0
    while i < size:
        l.append(random.randrange(0,max_value))
        i = i + 1
    return l

#test for build_random_list()
print(build_random_list(20,100))

def locate(l,value):
    index = 0
    while index <= len(l) - 1:
        if l[index] == value:
            return index
        elif l[index] != value and index != len(l) - 1:
            index = index + 1
        elif l[index] != value and index == len(l) - 1:
            return "-1"
    
 
#test for locate()
k = [1,2,623,7342,12,10,25,12,1,5,1]
print(locate(k,1))
print(locate(k,72))


def count(l,value):
    count = 0
    index_num = 0
    while index_num < len(l):
        if l[index_num] == value:
            count = count + 1
            index_num = index_num + 1
        else:
            index_num = index_num + 1
    return count

#test for count()
n = [1,2,63,8235,43,2,6,1,90,2]
print(count(n,2))
print(count(n,0))


def reverse(l):
    q = len(l)
    new_list = []
    for value in l:
        q = q - 1
        new_list.append(l[q])
    return new_list
    
#test for reverse()
m = [2,63,12,69,0,34,51,1]
print(reverse(m))

def isIncreasing(l):
    index = 0  
    while index != len(l) - 1 :
        if l[index] < l[index + 1]:
            index = index + 1          
        else:
            return False
    return True

#test for isIncreasing()
h = [1,5,9,12,16,53,100]
v = [43,43,62,23,9,0]
print(isIncreasing(h))
print(isIncreasing(v))

b = [1,2,3,4,5,4,3,2,1]

def palindrome(l):
    if l == reverse(l):   #calling previously written reverse() function
        return True
    else:
        return False

#test for palindrome()
print(palindrome(b))
print(palindrome(h))