#include <stdio.h>
#include <string.h>

int main()
{
    FILE *file = fopen("input/day5_input.txt", "r");
    char *line;
    char stacks[3][50] = {0};

    int current_stack = 0;
    while (fgets(line, 13, file))
    {
        if (line[0] == '\n')
            break;
        printf("%s\n", line);
        for (int i = 0; i < strlen(line); i++)
        {
            if (line[i] == ' ')
            {
                current_stack++;
                i += 3;
            }
            else if (line[i] == '[')
            {
                for (int j = 0; j < 49; j++)
                    stacks[current_stack][j + 1] = stacks[current_stack][j];
                stacks[current_stack][0] = line[i + 1];
                current_stack++;
                i += 3;
            }
            if (i < 50 && line[i] == '\n')
                current_stack = 0;
        }
    }

    for (int i = 0; i < 3; i++)
    {
        printf("%s\n", stacks[i]);
    }
    
    printf("end\n");

    return 0;
}