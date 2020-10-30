from matplotlib.pylab import *
import numpy as np

L = 1.04  # m
n = 20  #discretizacion de 20 intervalos (Malla)
dx = L / n

#x = linspace(0, L, n+1)
xu = 2

#arreglo con la solucion
Nt = 100000
#dt = 2.
#u_k = zeros((n+1))
#u_km1 = zeros((n+1))

#Condiciones de borde

bizq = 0       #Borde izq
bder = 0       #Borde izq
bin = 20       #Inicial

#Condicion inicial
#u_k[:] = 20   #25

K = 0.001495
c = 1.023
ρ = 2476
αf = K/(c * ρ)

#K = 79.5       # m^2/s
#c = 450.       # J/kg C
#ρ = 7800.      # kg/m^3
#α = K*dt/(c*ρ*dx**2)

#Coordenadas de nodos
nodos = [0.104, 0.208, 0.416]

#vector dt
vdt = [1, 5, 10, 50, 100]

figure()

for x in nodos:
    for dt in vdt:
        α = K * dt / (c * ρ * dx ** 2)
        Tem = Nt//dt #entero
        u = zeros((Tem, n + 1))

        #Condiciones
        u[:,0] = bizq
        u[:,-1] = bder
        u[0,1:n] = bin

        for k in range(Tem - 1):

            t = dt*k

            for i in range(1, n):
                u[k + 1, i] = u[k, i] + α * (u[k, i + 1] - 2 * u[k, i] + u[k, i - 1])

        vT = linspace(0, Nt, Tem)  #vector tem

        plot(vT, u[:, xu], label = f"Malla 20 Δt={dt} (s)")

#Fourier
    Fourier = []
    for time in range(Nt):
        sf = 0
        for ni in range(1, 50):
            sf += 40 * (1-(-1)**ni) / (ni*np.pi) * np.sin(ni*np.pi* x/L) * np.exp(-αf * (ni*np.pi/L)**2*time)
        Fourier.append(sf)

# Graficar
    vtf = linspace(0, Nt, Nt)

    plot(vtf, Fourier, label="Serie de Fourier", color="black", linestyle="--")

    title(f"x = {x}")
    xticks([18000, 36000, 54000, 72000, 90000], ["5", "10", "15", "20", "25"])
    legend()
    grid()
    ylabel("Temperatura [C]")
    xlabel("Tiempo [horas]")

    xu *= 2

    show()