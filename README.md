# Entrega 3 - Réplica de la sección 4.5 de la tésis de Alvaro Contreras:

* Verificar código 1-D replicando los resultados de la sección 4.5
* Específicamente replicar figuras 4.5 (pág 42) y figuras 4.7 (pág 44). Usar los mismos parámetros usados por Contreras. 
* Para poder discretizar las condiciones de borde del problema, es parecido al hehco por el profesor. donde el termino du/dt y d^2u/dx^2 son exactamnete los mismos de la expresion del profesor. Dado que las condiciones de borde u[0, x] = 20 y u[t, L] = 20 estan en la primera fila de la matriz y la ultima columna de la matriz , por lo que la "T" de solucion con cada iteracion va recorriendo de derecha a izquierda. Llegando a la primera columna, se describe la pendiente du/dx = (u[k,n-1]-u[k,n-1])/dx *[1]*, donde se da la condicion de borde du/dx[t,0]=5.  De esta manera, se puede ir llenando el vacio que genera la "T" en la matriz. Esto se hace usando la ecucacion *[1]* y despejar la condicion u[k,n-1]=dudx *x* dx-u[k,n]. de esta menera se llena la primera columna, distinto a como lo llena el ejemplo del profesor. De esta discretizacion, se obtiene el siguiente grafico. 

![WhatsApp Image 2020-10-29 at 9 21 10 PM](https://user-images.githubusercontent.com/69157203/97649159-62510d80-1a35-11eb-82a7-16c864e4afea.jpeg)


* Comente lo que ve. ¿Convergió la solución? ¿En qué casos cree ud. que se puede aplicar una condición de borde natural de el tipo estudiado hasta ahora?
