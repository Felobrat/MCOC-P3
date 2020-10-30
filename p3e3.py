from matplotlib.pylab import *
import numpy as np


L = 1.0
n = 100
dx = L/n

x = np.linspace(0,L,n+1)

#arreglo con la solucion

dt = 1.
Nt = 5000
u = np.zeros((Nt, n+1))

#condicion de borde
u[:,0] = 15.       #borde izquierdo
u[:,-1] = 5.       #borde derecho

#condicion inicial
u[0,1:n] = 35
K = 79.5        #m^2 /s
c = 450.        #J/kg C
ρ = 7800.       # kg / m^3
α = K*dt/(c*ρ*dx**2)



for k in range(Nt-1):
    t = dt*k
    print(f"k={k} t = {t}")
    for i in range(1,n):
        u[k+1,i] = u[k,i] + α*(u[k,i+1] - 2*u[k,i] + u[k,i-1])
        
    if k % 200 ==0:
        plot(x,u[k,:])
title("k = {} t={} s" .format(k,k*dt))
show()
