#include <stdio.h>
#include <time.h>

void hanoi(int n, char from, char to, char aux) {
    if (n == 1) {
        // printf("Mover disco de %c a %c\n", from, to);
        return;
    }
    hanoi(n-1, from, aux, to);
    // printf("Mover disco de %c a %c\n", from, to);
    hanoi(n-1, aux, to, from);
}

int main() {
    int n = 20;
    clock_t start, end;
    double tiempo;

    start = clock();
    hanoi(n, 'A', 'C', 'B');
    end = clock();

    tiempo = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("Torres de Hanoi con %d discos completado.\n", n);
    printf("Tiempo en C: %f segundos\n", tiempo);

    return 0;
}
