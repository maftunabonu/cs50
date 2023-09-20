#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (1 > height || height > 9);
    for (int i = 1; i <= height; i++)
    {
        for (int j = 1; j < height + i + 2; j++)
        {
            if (j == height + 1)
            {
                printf("  ");
            }
            else if (j > height - i)
            {
                printf("#");
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }
}