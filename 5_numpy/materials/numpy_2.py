import numpy as np
from matplotlib import pyplot as plt

# histogram
a = np.random.randint(30, size=50)
plt.figure(1)
plt.hist(a, bins=np.arange(0, 31, 5))
plt.title('histogram')
plt.show()

# np.any - an 'or' gate
a = np.random.normal(loc=0.5, scale=1, size=20)
# with single condition
print(np.any(a > 1.5), len(a[a > 1.5]))
# with complex condition - notice 'c' like syntax
print(np.any((a > 0) & (a < 1)), len(a[(a > 0) & (a < 1)]))

# np.all - an 'and' gate
print(np.all(a > -1), len(a[a > -1]), len(a))
# with complex condition - notice 'c' like syntax
print(np.all((a > -1) & (a < 1.5)), len(a[(a > -1) & (a < 1.5)]), len(a))

# Mathematical Functions with np.linspace()
# example 1
x = np.linspace(0, 2 * np.pi, 100)
f = np.sin(x)
plt.figure(2)
plt.plot(x, f)
plt.show()

# example 2:
x_ = np.linspace(-5, 5, 50)
y_ = 4 * (x_ ** 3) + 2 * (x_ ** 2) + 5 * x_
plt.figure(3)
plt.plot(x_, y_)
plt.show()

# Plotting Mathematical Functions With np.meshgrid and plt.contourf
# numpy meshgrid
# create a rectangular grid out of an array of x values and an array of y valu
# in the example above a rectangulatr grid of 3x5 is created
n1, n2 = 5, 3
a = np.linspace(0, 1, n1)
b = np.linspace(0, 1, n2)
aa, bb = np.meshgrid(a, b)
print(aa)
print(bb)
z = 5 * aa + bb ** 2
plt.contourf(a, b, z)

# plotting f(x)= Sinus(x^2+y^2)/(x^2+y^2)
n = np.arange(-5, 5, 0.1)
m = np.arange(-5, 5, 0.1)
x, y = np.meshgrid(n, m)
c = np.sin(x ** 2 + y ** 2) / (x ** 2 + y ** 2)
z = plt.contourf(n, m, c)
plt.show()

# another example
x = np.linspace(-5, 5, 11)
y = np.linspace(-5, 5, 11)
X, Y = np.meshgrid(x, y)
Z = X ** 2 + Y ** 2
fig = plt.figure()
plt.contourf(X, Y, Z, cmap='plasma')
plt.axis('scaled')
plt.colorbar()
plt.savefig('contour1.png')
plt.show()
