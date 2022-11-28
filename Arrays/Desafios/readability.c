#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int main(void)
{
    string text = get_string("Text: ");

    int letters = 0;
    int words = 0;
    int sentences = 0;
    for(int i = 0, tamanhoString = strlen(text); i <= tamanhoString; i++)
    {
        if(isalpha(text[i]))
        {
            letters++;
        }
        else if(isspace(text[i]))
        {
            words++;
        }
        else if((text[i] == '.' || text[i] == '!' || text[i] == '?'))
        {
            sentences++;
        }
    }

    float L = (letters / (words + 1.0)) * 100;
    float S = (sentences / (words + 1.0)) * 100;
    int coleman_liau_index = round((0.0588 * L) - (0.296 * S) - 15.8);

    if(coleman_liau_index < 1)
    {
        printf("Before Grade 1");
    }
    else if(coleman_liau_index >= 16)
    {
        printf("Grade 16+");
    }
    else
    {
        printf("Grade %i", coleman_liau_index);
    }
    printf("\n");
}