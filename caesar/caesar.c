#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    // Make sure program was run with just one command-line argument
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Make sure every character in argv[1] is a digit
    string passedInArgument = argv[1];
    for (int i = 0; i < strlen(passedInArgument); i++)
    {
        char character = passedInArgument[i];

        if (!isdigit(character))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    // Convert argv[1] from a `string` to an `int`
    int caesarCount = atoi(passedInArgument);

    // Prompt user for plaintext
    string plaintext = get_string("plaintext: ");

    // For each character in the plaintext:
    for (int i = 0; i < strlen(plaintext); i++)
    {
        char character = plaintext[i];

        if (!isdigit(character))
        {
            // Rotate the character if it's a letter
            for (int z = 0; z < caesarCount; z++)
            {
                character = plaintext[i];
                if ((character >= 'a' && character < 'z') || (character >= 'A' && character < 'Z'))
                {
                    // change the letter in the string not the variable character
                    plaintext[i]++;
                }
                else if (character == 'z')
                {
                    plaintext[i] = 'a';
                }
                else if (character == 'Z')
                {
                    plaintext[i] = 'A';
                }
            }
        }
    }

    printf("ciphertext: %s\n", plaintext);
}
