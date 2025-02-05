#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    string word = get_string("Text: ");
    int bit_counter;
    for (int i = 0; i < strlen(word); i++)
    {
        int character = word[i];

        for (bit_counter = 7; bit_counter > -1; bit_counter--)
        {
            // shift the character bit over and compare it to a 1
            print_bulb((character >> bit_counter) & 1);
        }
        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
