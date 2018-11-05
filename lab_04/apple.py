def countApplesAndOranges(s,t,a,b,apples,oranges):
    count_apples = 0
    count_oranges = 0
    
    for i in apples:
        if a+i in range(s,t+1):
            count_apples = count_apples + 1
            
    for i in oranges:
        if b+i in range(s,t+1):
            count_oranges = count_oranges + 1
    
    return str(count_apples) + ", " + str(count_oranges)
        
        
    

s = 5
t = 10
a = 2
b = 12

apples = [2,-5,6,8,4]
oranges = [5,-3,1,-7]

print(countApplesAndOranges(s,t,a,b,apples,oranges))