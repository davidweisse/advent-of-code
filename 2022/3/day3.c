#include <stdio.h>
#include <string.h>

int main()
{
    FILE *file = fopen("input/day3_input.txt", "r");
    char line[50];
    char str[3][50];
    int sum1 = 0, sum2 = 0, counter = 0;

    while (fgets(line, 50, file))
    {
        int sum = 0;
        for (int i = 0; i < (strlen(line) - 1) / 2; i++)
        {
            for (int j = (strlen(line) - 1) / 2; j < strlen(line) - 1; j++)
                if (line[i] == line[j])
                    sum = (line[i] > 97) ? line[i] - 96 : line[i] - 38;
            if (sum > 0)
                break;
        }
        sum1 += sum;
        sum = 0;
        strcpy(str[counter], line);
        if (counter == 2)
        {
            for (int i = 0; i < strlen(str[0]) - 1; i++)
            {
                for (int j = 0; j < strlen(str[1]) - 1; j++)
                    for (int k = 0; k < strlen(str[2]) - 1; k++)
                        if (str[0][i] == str[1][j] && str[0][i] == str[2][k])
                            sum = (str[0][i] > 97) ? str[0][i] - 96 : str[0][i] - 38;
                if (sum > 0)
                    break;
            }
            sum2 += sum;
        }
        
        counter = (counter + 1) % 3;
    }

    printf("Sol1: %d\n", sum1);
    printf("Sol2: %d\n", sum2);

    return 0;
}