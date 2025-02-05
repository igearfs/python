#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string testText = get_string("Text: ");

    int lettersPer100Words = count_letters(testText);
    int wordCountBySpacesOrReturn = count_words(testText);
    int sentancesPer100Words = count_sentences(testText); // so we count the first word

    // where L is the average number of letters per 100 words in the text,
    // and S is the average number of sentences per 100 words in the text.
    // index = 0.0588 * L - 0.296 * S - 15.8
    // 65 letters per 14 words is an average of about 464.29 letters per 100 words (because 65 / 14 * 100 = 464.29
    // And 4 sentences per 14 words is an average of about 28.57 sentences per 100 words (because 4 / 14 * 100 = 28.57).

    float totalLettersPer100 = 0.0;
    float totalSentancesPer100 = 0.0;
    if (wordCountBySpacesOrReturn < 100)
    {
        totalLettersPer100 = ((float) lettersPer100Words / (float) wordCountBySpacesOrReturn) * 100;
        totalSentancesPer100 = ((float) sentancesPer100Words / (float) wordCountBySpacesOrReturn) * 100;
    }

    float gradeResultAsfloat = 0.0588 * totalLettersPer100 - 0.296 * totalSentancesPer100 - 15.8;
    int index = round(gradeResultAsfloat);
    string response = "";
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 15)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

int count_letters(string text)
{
    int lettersPer100Words = 0;

    char character;
    for (int i = 0; i < strlen(text); i++)
    {
        character = text[i];
        if (isupper(character) || islower(character))
        {
            // printf("lettersPer100Words::%c\n" , character);
            lettersPer100Words++;
        }
    }
    return lettersPer100Words;
}

int count_words(string text)
{
    int wordCountBySpacesOrReturn = 1;

    char character;
    for (int i = 0; i < strlen(text); i++)
    {
        character = text[i];
        if (character == ' ' || character == '\0')
        {
            // printf("wordCountBySpacesOrReturn::%c\n" , character);
            wordCountBySpacesOrReturn++;
        }
    }
    return wordCountBySpacesOrReturn;
}

int count_sentences(string text)
{
    int sentancesPer100Words = 0;
    char character;
    for (int i = 0; i < strlen(text); i++)
    {
        character = text[i];
        if (character == '.' || character == '!' || character == '?')
        {
            // printf("sentancesPer100Words::%c\n" , character);
            sentancesPer100Words++;
        }
    }

    return sentancesPer100Words;
}
