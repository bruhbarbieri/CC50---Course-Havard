#include <stdio.h>
#include <cs50.h>
#include <math.h>

float get_valor();

int main(void)
{
    int c25 = 0;
    int c10 = 0;
    int c5 = 0;
    int c1= 0;

    float valor = get_valor();
    while(valor < 0) {
        valor = get_valor();
    }

    int centavos = valor * 100;

    c25 = centavos / 25;
    c10 = (centavos - (c25 * 25)) / 10;
    c5 = (centavos - (c25 * 25) - (c10 * 10)) / 5;
    c1 = centavos - (c25 * 25) - (c10 * 10) - (c5 * 5);

    printf("%i\n", c25 + c10 + c5 + c1);

}

float get_valor() {
    return get_float("Valor: ");
}