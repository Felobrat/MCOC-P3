from matplotlib.pylab import *

L = 1.0
n = 100 #discretizacion de 100 intervalos
dx = L / n

x = linspace(0, L, n+1)

#arreglo con la solucion
dt = 2.
Nt = 50000
u = zeros((Nt, n+1))



#Condiciones de borde
u[:,0] = 20.       #borde izquierdo
u[:,-1] = 20.       #borde derecho
dudx0 = 5          #condicion de borde de primera derivada

#Condicion inicial
u[0, 1:n] = 20

K = 79.5 # m^2 / s
c = 450.        #J/kg C
ρ = 7800.       # kg / m^3
α = K*dt/(c*ρ*dx**2)        #m^2 /s


for k in range(Nt-1):
	t = dt*k
	print(f"k = {k} t = {t}")
	u[k,0] = u[k,1] - dudx0 * dx
	for i in range(1,n):
		u[k+1, i] = u[k,i] + α*(u[k, i+1] - 2*u[k, i] + u[k, i-1])

	if k % 1000 == 0:
		plot(x,u[k,:])

title ("k = {}  t = {} s".format(k, k*dt))
show ()
