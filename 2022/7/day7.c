#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main()
{
    FILE *file = fopen("input/day7_input.txt", "r");
    int stack[20] = {0}, sizes[200] = {0};
    char line[30];
    while (fgets(line, 30, file))
    {
        if (!strcmp(line, "$ cd ..\n"))
        {
            int size = stack[stack[0]];
            stack[0]--;
            sizes[0]++;
            sizes[sizes[0]] = size;
            stack[stack[0]] += size;
        }
        else if (!strncmp(line, "$ cd ", 5))
        {
            stack[0]++;
            stack[stack[0]] = 0;
        }
        else if (isdigit(line[0]))
        {
            int size;
            sscanf(line, "%d", &size);
            stack[stack[0]] += size;
        }
    }
    
    while (stack[0] > 0)
    {
        sizes[0]++;
        sizes[sizes[0]] = stack[stack[0]];
        stack[0]--;
        if (stack[0] > 0)
            stack[stack[0]] += sizes[sizes[0]];
    }
    
    int sum = 0;
    int min = sizes[sizes[0]];
    for (int i = 1; i < sizes[0] + 1; i++)
    {
        if (sizes[i] <= 100000)
            sum += sizes[i];
        if (sizes[i] >= sizes[sizes[0]] - 40000000 && sizes[i] < min)
            min = sizes[i];
    }
    printf("Sol1: %d\n", sum);
    printf("Sol2: %d\n", min);

    return 0;
}