# Kaitlyn Zhen and Matthew Barron

def mysqrt(n):
    guess = 1
    new_guess = 0
    while new_guess**2 != n:
           if new_guess**2 != n:
               new_guess = (guess + (n/guess))/2
               print(new_guess)
               if new_guess==guess:
                   return new_guess
               else:
                   guess = new_guess
    
print(mysqrt(4))

print(mysqrt(12386))
