Estos programas muestran como un mismo problema recursivo que es las Torres de Hanoi, se resuelve mucho más rapido en un lenguaje compilado (C) que en un lenguaje interpretado (Python). La diferencia es que traduce directamente el codigo a instrucciones de maquina, mientras que el interprete ejecuta linea por linea. Así, aunque Python resulta mas simple, C ofrece un rendimiento mayor, lo que evidencia la ventaja de los lenguajes compilados en aplicaciones que requieren alta eficiencia.

Salida de la terminal:

ubuntu@ubuntu:~$ ./hanoi 
Torres de Hanoi con 20 discos completado.
Tiempo en C: 0.008089 segundos
ubuntu@ubuntu:~$ python3 hanoi.py 
Torres de Hanoi con 20 discos completado.
Tiempo en Python: 0.07630419731140137 segundos

Se evidencian los tiempos:
C= 0.008089 segundos
Python= 0.0763 segundos
