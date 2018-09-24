#Kaitlyn Zhen and Matthew Barron

def fizzbuzz(max_value):

    i = 0
    count = 0
    while i <= max_value-1:
        i = i + 1
        if i % 3 == 0 and i % 5 != 0:
            print("fizz")
        elif i % 5 == 0 and i % 3 != 0:
            print("buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
            count = count + 1
        else:
            print(i)
    return count 

print(fizzbuzz(100))