#include <stdio.h>

int main()
{
    FILE *file = fopen("input/day4_input.txt", "r");
    int x[4];
    int count1 = 0, count2 = 0;

    while (!feof(file))
    {
        fscanf(file, "%d-%d,%d-%d\n", &x[0], &x[1], &x[2], &x[3]);

        if ((x[0] <= x[2] && x[1] >= x[3]) || (x[0] >= x[2] && x[1] <= x[3]))
            count1++;
        if ((x[0] <= x[2] && x[1] >= x[2]) || (x[2] <= x[0] && x[3] >= x[0]))
            count2++;
    }

    printf("Sol1: %d\n", count1);
    printf("Sol2: %d\n", count2);

    return 0;
}