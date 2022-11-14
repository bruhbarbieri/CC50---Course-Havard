#include <cs50.h>
#include <stdio.h>

int main (void)
{
    long x = get_long("x: ");

    long y = get_long("y: ");

    float z = (float) x / (float) y;

    if (x < y)
    {
        printf("x is less than y\n");
    }
    else if (x > y)
    {
        printf("x is greater than y\n");
    }
    else
    {
        printf("x is equal than y\n");
    }
}