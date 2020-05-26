## Solving non-linear convection equation in 2D
## May 2020.

# importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# variables and discritization parameters

nt=100
nx=101
ny=101

dx=2/(nx-1)
dy=2/(ny-1)
sigma=0.2
dt=sigma*dx

x = np.linspace(0, 2, nx)
y = np.linspace(0, 2, ny)

u = np.ones((ny, nx))
v = np.ones((ny, nx))
un = np.ones((ny, nx))
vn = np.ones((ny, nx))
uf=np.ones((nt,nx,ny))
vf=np.ones((nt,nx,ny))

# assigning initial conditions
u[int(0.75 / dy):int(1.25 / dy + 1),int(0.75 / dx):int(1.25 / dx + 1)] = 2.5
v[int(0.75 / dy):int(1.25 / dy + 1),int(0.75 / dx):int(1.25 / dx + 1)] = 2.5

###(ploting ICs)
fig = plt.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
X, Y = np.meshgrid(x, y)
ax.plot_surface(X, Y, u[:], cmap=cm.jet)
plt.title('U')
plt.xlabel('X')
plt.ylabel('Y');
fig.savefig('U-I.C.png', bbox_inches='tight')

##loop across number of time steps
for n in range(nt):
    un = u.copy()
    vn = v.copy()
    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            u[i, j] = (un[i, j] - (un[i, j] * dt / dx * (un[i, j] - un[i - 1, j])) -
                       vn[i, j] * dt / dy * (un[i, j] - un[i, j - 1]))
            v[i, j] = (vn[i, j] - (un[i, j] * dt / dx * (vn[i, j] - vn[i - 1, j])) -
                       vn[i, j] * dt / dy * (vn[i, j] - vn[i, j - 1]))

    # Velocity boundary conditions
    u[0, :] = 1
    u[-1, :] = 1
    u[:, 0] = 1
    u[:, -1] = 1

    v[0, :] = 1
    v[-1, :] = 1
    v[:, 0] = 1
    v[:, -1] = 1

# plotting U field as a Surface

fig = plt.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
X, Y = np.meshgrid(x, y)
ax.plot_surface(X, Y, u, cmap=cm.jet)
fig.savefig('U.png', bbox_inches='tight')