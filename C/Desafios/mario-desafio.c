#include <stdio.h>
#include <cs50.h>

int get_altura();

int main(void)
{
    int altura = get_altura();
    while(altura < 1 || altura > 8) {
        altura = get_altura();
    }

    int coluna = 1;
    while (coluna <= altura) {
        int espaços = altura - coluna;
        for(int intervalo = 0; intervalo < espaços; intervalo++) {
            printf(" ");
        }
        for(int bloco = 0; bloco < coluna; bloco++) {
            printf("#");
        }
        printf("  ");

        for(int bloco = 0; bloco < coluna; bloco++) {
            printf("#");
        }
        printf("\n");
        coluna++;
    }

}

int get_altura() {
    return get_int("Altura: ");
}