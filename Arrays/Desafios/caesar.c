#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, string argv[])
{

    if(argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    for(int i = 0, tamanhoString = strlen(argv[1]); i < tamanhoString; i++)
    {

        if(isalpha(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }


    int transfInt = atoi(argv[1]);
    string text = get_string("plaintext: ");
    printf("ciphertext: ");
    for(int j = 0, tamanhoString = strlen(text); j < tamanhoString; j++)
    {

        if(islower(text[j]))
        {
            printf("%c", (((text[j] - 97) + transfInt) % 26) + 97);
        }
        else if(isupper(text[j]))
        {
            printf("%c", (((text[j] - 65) + transfInt) % 26) + 65);
        }
        else
        {
            printf("%c", text[j]);
        }
    }
    printf("\n");
    return 0;
}