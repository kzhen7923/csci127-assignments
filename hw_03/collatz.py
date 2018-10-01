#Kaitlyn Zhen and Matthew Barron

def F(n):
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            print(n)
        elif n % 2 != 0:
            n = (3 * n) + 1
            print(n)
        else:
            print(n)
            
F(6)