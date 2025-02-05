#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get size of grid
    int sizeOfPyramid;

    do
    {
        sizeOfPyramid = get_int("Size: ");
    }
    while (sizeOfPyramid < 1 || sizeOfPyramid > 8);

    // Print grid of bricks
    for (int row = 0; row < sizeOfPyramid; row++)
    {
        for (int blankSpace = 1; blankSpace < sizeOfPyramid - row; blankSpace++)
        {
            printf(" ");
        }

        for (int j = 0; j < row + 1; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
