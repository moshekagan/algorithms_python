import numpy as np
from matplotlib import pyplot as plt

# 1.
x = np.linspace(-np.pi, np.pi, 1000)
f = np.exp(x/2)*np.sin(x)-x/2

# integral from -pi to pi equals to (8/5)*sin(pi/2) = 3.6821


def trapez(x, f):
	dx = x[1]-x[0]
	f_pairs_sum = f[: -1] + f[1:]
	areas = f_pairs_sum*dx/2
	area = np.sum(areas)
	areas = np.cumsum(areas)

	return areas, area


def formula_integral(x, f):
	dx = x[1] - x[0]
	area = dx*((f[0] + f[-1]) / 2 + np.sum(f[1:-1]))

	return area


trapez_integral, trapez_value = trapez(x, f)

formula_value = formula_integral(x, f)

print(trapez_value)
print(formula_value)
# print(trapez_integral)

fig1 = plt.figure(1)
plt.plot(x, f)

fig2 = plt.figure(2)
plt.plot(x[:-1], trapez_integral)
plt.show()
