import time

def hanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        # print(f"Mover disco de {from_rod} a {to_rod}")
        return
    hanoi(n-1, from_rod, aux_rod, to_rod)
    # print(f"Mover disco de {from_rod} a {to_rod}")
    hanoi(n-1, aux_rod, to_rod, from_rod)

n = 20

inicio = time.time()
hanoi(n, 'A', 'C', 'B')
fin = time.time()

print(f"Torres de Hanoi con {n} discos completado.")
print(f"Tiempo en Python: {fin - inicio} segundos")

