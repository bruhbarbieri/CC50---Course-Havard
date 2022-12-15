#include <stdio.h>

void swap(int *a, int *b);

int main (void)
{
    int x = 1;
    int y = 2;

    printf("x is %p, y is %p\n", &x, &y);
    printf("x is %i, y is %i\n", x, y);
    swap(&x, &y);
    printf("x is %i, y is %i\n", x, y);
}

void swap(int *a, int *b) //se não for pornteiro, não vai mudar as variaveis x e y no main
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}