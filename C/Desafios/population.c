#include <stdio.h>
#include <cs50.h>
#include <math.h>

int get_population();
int get_endSize();

int main(void)
{
    int population = get_population();
    int endSize = get_endSize();
    int years = 0;

    while(population < endSize) {
        population = population + (round(population / 3) - round(population / 4));
        years++;
    }

    printf("Years: %i\n", years);
}

int get_population() {
    return get_int("População Inicial: ");
}

int get_endSize() {
    return get_int("População Final: ");
}