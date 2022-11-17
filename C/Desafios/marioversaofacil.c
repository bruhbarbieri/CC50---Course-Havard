#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int altura;
    do
    {
        altura = get_int("Width: ");
    }
    while (altura < 1 || altura > 8);

    for (int coluna = 0; coluna < altura; coluna++)
    {
        for (int bloco = 0; bloco <= coluna; bloco++)
        {
        printf("#");
        }
        printf("\n");
    }
}