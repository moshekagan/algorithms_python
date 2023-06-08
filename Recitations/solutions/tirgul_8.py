from matplotlib import pyplot as plt
import numpy as np

def stair(x0, y0, xf, yf):
    x = np.array([x0,xf, xf, x0, x0])
    y = np.array([y0, y0, yf, yf, y0])
    plt.plot(x, y)
    plt.show()


x = np.arange(0, 2*2*np.pi, 0.000001) #קפיצות קטנות בין הנקודות
y = 3*np.sin(x) + np.cos(2*x)
plt.plot(x, y)
plt.show()

x = np.linspace(0,  2*2*np.pi, 100) #100-כמה אלמנטים
y = 3*np.sin(x) + np.cos(2*x)
plt.plot(x, y)
plt.show()

x = np.linspace(-10, 10, 1000)
y = np.linspace(-5, 5, 1000)
mat_x, mat_y = np.meshgrid(x, y)
mat_z = mat_x**2 + mat_y**3 + 2*mat_x*mat_y
plt.contour(mat_x, mat_y, mat_z)
plt.show()


'from the mudele'
import numpy as np
from matplotlib import pyplot as plt

def stair (x0, y0, xf, yf):
    x = [x0, xf, xf, x0, x0]
    y = [y0, y0, yf, yf, y0]
    plt.plot(x,y, 'b')



stair(0,0,1,1)
plt.show()
# b
# num = input('enter number of stairs')
num = 8
# plt.clf()
for i in range(num):
    stair(i, 0, 2*num-i-1, i+1)

plt.show()


# 2

x = np.arange(0, 2*2*np.pi, 0.01)
y = 3*np.sin(x) + np.cos(2*x)
plt.plot(x,y)
plt.show()

# 3
res = 0.1
x = np.arange(-10, 10, res)
y = np.arange(-5, 5, res)
x_mat, y_mat = np.meshgrid(x, y)

z_mat = x_mat**2+y_mat**3+2*x_mat*y_mat
ax = plt.axes(projection ='3d')
ax.plot_surface(x_mat, y_mat, z_mat)
plt.show()