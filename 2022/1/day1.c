#include <stdio.h>
#include <stdlib.h>

int cmpfunc(const void *a, const void *b)
{
    return (*(int *)b - *(int *)a);
}

int main()
{
    FILE *file = fopen("input/day1_input.txt", "r");
    char buffer[10];
    int nums[2263];
    int len = sizeof(nums) / sizeof(int);

    int i = 0;
    while (fgets(buffer, 10, file))
    {
        nums[i] = atoi(buffer);
        i++;
    }

    int *sums = malloc(1000 * sizeof(int));
    int number_sums = 0;
    int current_sum = 0;

    for (int i = 0; i < len; i++)
    {
        if (nums[i] != 0)
            current_sum += nums[i];
        else
        {
            *(sums + number_sums) = current_sum;
            current_sum = 0;
            number_sums++;
        }
    }

    sums = realloc(sums, number_sums * sizeof(int));

    qsort(sums, number_sums, sizeof(int), cmpfunc);

    printf("Sol1: %d\n", sums[0]);
    printf("Sol2: %d\n", sums[0] + sums[1] + sums[2]);

    return 0;
}