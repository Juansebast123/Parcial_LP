El programa implementa un Autómata Finito Determinista (AFD) que se configura por un archivo de texto (Conf.txt) y evalua una lista de cadenas (Cadenas.txt), donde indica si acepta o NO acepta segun las reglas establecidas.
- a's preceden b's, b's preceden c's
- Es posible que no hayan a's, b's o c's en la cadena.

En el Conf.txt se observa la configuracion de: estados, alfabeto, inicial, finales. Estos son leidos en el .py a partir de la linea en la que se encuentran ubicados en Conf.txt. Es decir: 
- estados=linea(0) y son separados por una ','.
- alfabeto=linea(1) y son separados por una ','.
- inicial=linea(2) (solo es uno).
- finales=linea(3) y son separados por una ','.

Las reglas del AFD es que debe ser posible que haya una cadena vacia, por lo que se implementa: if cadena == ""; 

Explicacion de como funciona el AFD:
 
Cadena: aaabbbcc
Estado inicial: q0
- Lee 'a' → (q0, a) = sigue en q0
- Lee 'a' → (q0, a) = sigue en q0
- Lee 'a' → (q0, a) = sigue en q0
- Lee 'b' → (q0, b) = pasa a q1
- Lee 'b' → (q1, b) = sigue en q1
- Lee 'b' → (q1, b) = sigue en q1
- Lee 'c' → (q1, c) = pasa a q2
- Lee 'c' → (q2, c) = sigue en q2
aaabbbcc -> acepta.


