# Para resolver esta pregunta se usará el algoritmo de Miller-Rabin

El número a ser usado es 141025414102541410254

Dado que es un número par, es trivial que es un número compuesto. Por ello se considerará el número 141025414102541410253.

Se codeó el problema en el archivo `pregunta_1.py` y se obtiene respuesta de que el número no es primo. El número de iteraciones fue 1.

El valor de $a =87844969466995113984$, luego, $t = 141025414102541410252$, s = 0. Para el momento que se entra al loop, $s = 1$ y $t = 70512707051270705126$. El chequeo $t % 2 == 1$ es falso, así que $s = 2$, $t = 35256353525635352563$. En este caso, t es impar así que salimos del if. 
Calculando el valor de $expomod(a,t,n)$ tenemos $x = 62620277057575132968$ dado que no es ni uno, ni 141025414102541410253, seguimos. Para este punto, $s = 2$, así que se ejecuta el último bucle dos veces donde se tiene en la primera iteración que $x = 72204246510758848042$ y por último $x = 38931724659366623800$, dado que se acabaron las iteraciones se retorna False.

Como se retorna False, el if de `millerRabRep` retorna True y finalmente la ejecución retorna False a la primera iteración, por lo tanto no fue necesario ejecutarlo 10 veces.
