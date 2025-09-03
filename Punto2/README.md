El programa implementa un Autómata Finito Determinista (AFD) qrealizado en python que evalua una lista de 5 ID (pruebas.txt), donde indica si ACEPTE o NO ACEPTE segun las reglas establecidas.
- Debe empezar con una letra [A-Za-z].
- Despues de la primera letra puede ir un numero entero o una letra [A-Za-z0-9].

Explicacion de como funciona el AFD:
 
Cadena: se0607
Estado inicial: q0
- Lee 's' → (q0, letra) = pasa a q1
- Lee 'e' → (q0, letra) = sigue en q1
- Lee '0' → (q0, numero) = sigue en q1
- Lee '6' → (q0, numero) = sigue en q1
- Lee '0' → (q1, numero) = sigue en q1
- Lee '7' → (q1, numero) = sigue en q1
