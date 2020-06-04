#5x3 +3x2 -2x +5

def wielomian(x):
  return lambda x : ((5*(x**3)) - 3 * (x**2)) - (2*x) + 5

#LUB

wielomian1 = lambda x : ((5*(x**3)) - 3 * (x**2)) - (2*x) + 5
print(wielomian1(2))

