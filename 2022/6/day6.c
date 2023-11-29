#include <stdio.h>

int main()
{
    FILE *file = fopen("input/day6_input.txt", "r");
    char input[5000];
    fgets(input, 5000, file);
    
    int i, disjoint;
    for (i = 0; input[i] != '\0'; i++)
    {
        disjoint = 1;
        for (int j = 0; j < 4; j++)
            for (int k = 0; k < 4; k++)
                if (j != k && input[i + j] == input[i + k])
                    disjoint = 0;
        if (disjoint == 1)
            break;
    }
    printf("Sol1: %d\n", i + 4);
    for (i = 0; input[i] != '\0'; i++)
    {
        disjoint = 1;
        for (int j = 0; j < 14; j++)
            for (int k = 0; k < 14; k++)
                if (j != k && input[i + j] == input[i + k])
                    disjoint = 0;
        if (disjoint == 1)
            break;
    }
    printf("Sol1: %d\n", i + 14);

    return 0;
}