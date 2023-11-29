#include <stdio.h>

int main()
{
    FILE *file = fopen("input/day2_input.txt", "r");
    char line[10];
    int score1 = 0, score2 = 0;
    char opp, you;

    while (fgets(line, 10, file))
    {
        sscanf(line, "%c %c", &opp, &you);
        opp -= 65;
        you -= 88;

        score1 += you + 1;
        if ((opp + 1) % 3 == you % 3)
            score1 += 6;
        else if (opp == you)
            score1 += 3;

        if (you == 0)
            score2 += (opp != 0 ? opp - 1 : opp + 2) + 1;
        else if (you == 1)
            score2 += opp + 4;
        else
            score2 += ((opp + 1) % 3) + 7;
    }

    printf("Sol1: %d\n", score1);
    printf("Sol2: %d\n", score2);
    return 0;
}