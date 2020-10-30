# Entrega 3 - Réplica de la sección 4.5 de la tésis de Alvaro Contreras:

* En los codigos p3e3_1.py y p3e3_2.py se obtienen los resultados obtemidos por Contreras.

* Se obtienen los mismos resultados de Contreras en los graficos a continuacion:


*Figuras 4.5


![WhatsApp Image 2020-10-29 at 10 21 30 PM](https://user-images.githubusercontent.com/69157203/97649861-1f903500-1a37-11eb-81f4-ef851e2ce226.jpeg)
![WhatsApp Image 2020-10-29 at 10 20 56 PM](https://user-images.githubusercontent.com/69157203/97649864-2028cb80-1a37-11eb-89df-32f53cf18dc0.jpeg)
![WhatsApp Image 2020-10-29 at 10 20 49 PM](https://user-images.githubusercontent.com/69157203/97649865-21f28f00-1a37-11eb-8602-66d47d1fb427.jpeg)

*Figuras 4.7


![Figure 2020-10-29 224117](https://user-images.githubusercontent.com/69157203/97650254-08057c00-1a38-11eb-9de0-96a1dc26809e.png)
![Figure 2020-10-29 224133](https://user-images.githubusercontent.com/69157203/97650256-0936a900-1a38-11eb-9fb9-eef0dbf8ee94.png)
![Figure 2020-10-29 224138](https://user-images.githubusercontent.com/69157203/97650258-0a67d600-1a38-11eb-8a6c-09193acf38dd.png)


* Para poder discretizar las condiciones de borde del problema, es parecido al hehco por el profesor. donde el termino du/dt y d^2u/dx^2 son exactamnete los mismos de la expresion del profesor. Dado que las condiciones de borde u[0, x] = 20 y u[t, L] = 20 estan en la primera fila de la matriz y la ultima columna de la matriz , por lo que la "T" de solucion con cada iteracion va recorriendo de derecha a izquierda. Llegando a la primera columna, se describe la pendiente du/dx = (u[k,n-1]-u[k,n-1])/dx *[1]*, donde se da la condicion de borde du/dx[t,0]=5.  De esta manera, se puede ir llenando el vacio que genera la "T" en la matriz. Esto se hace usando la ecucacion *[1]* y despejar la condicion u[k,n-1]= u[k,n] - dudx *x* dx. de esta menera se llena la primera columna, distinto a como lo llena el ejemplo del profesor. De esta discretizacion, se obtiene el siguiente grafico. 

![WhatsApp Image 2020-10-29 at 9 21 10 PM](https://user-images.githubusercontent.com/69157203/97649159-62510d80-1a35-11eb-82a7-16c864e4afea.jpeg)


* Comente lo que ve. ¿Convergió la solución? ¿En qué casos cree ud. que se puede aplicar una condición de borde natural de el tipo estudiado hasta ahora?
