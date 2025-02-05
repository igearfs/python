#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int startSize;

    do
    {
        startSize = get_int("Start size: ");
    }
    while (startSize < 9);

    // TODO: Prompt for end size
    int endSize;

    do
    {
        endSize = get_int("End size: ");
    }
    while (endSize < startSize);
    // TODO: Calculate number of years until we reach threshold

    // count the years
    int yearCounter = 0;

    for (; startSize < endSize; yearCounter++)
    {
        startSize += ((startSize / 3) - (startSize / 4));
    }

    // TODO: Print number of years
    printf("Years: %i\n", yearCounter);
}
