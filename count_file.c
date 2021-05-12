#include <stdio.h>
#include <stdlib.h>


int main()
{
    FILE * file, *file2;
    char path[100] = "words.txt";
    char ch;
    int characters, words, lines;
    file = fopen(path, "r");
    if (file == NULL)
    {
        printf("\nUnable to open file.\n");
        printf("Please check if file exists and you have read privilege.\n");
        exit(EXIT_FAILURE);
    }
    characters = 0;
    words = 0;
    lines = 0;
    char capsWord[100];
    int i = 0;
    int j = 0;
    while ((ch = fgetc(file)) != EOF)
    {
        characters++;
        if (ch == '\n' || ch == '\0')
            lines++;
        if (ch == ' ' || ch == '\t' || ch == '\n' || ch == '\0')
            words++;
    }
    if (characters > 0)
    {
        words++;
        lines++;
    }
    printf("\n");
    printf("Total characters = %d\n", characters);
    printf("Total words      = %d\n", words);
    printf("Total lines      = %d\n", lines);
    fclose(file);
    return 0;
}