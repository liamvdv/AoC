#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_DIGIT_BUF 64

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Usage: ./main <filepath>\n");
        return 1;
    }
    FILE* fp;
    char* line = NULL;
    
    size_t len = 0;
    ssize_t read;

    fp = fopen(argv[1], "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    int horizontal = 0;
    int depth = 0;

    char digit_buf[MAX_DIGIT_BUF];
    while ((read = getline(&line, &len, fp)) != -1) {
        // line still contains newline, read == strlen()
        int lend = read - 1;
        if (strncmp(line, "forward", 7) == 0) {
            strncpy(digit_buf, line + 8, lend);
            horizontal += atoi(digit_buf);
        } 
        else if (strncmp(line, "down", 4) == 0) {
            strncpy(digit_buf, line + 5, lend);
            depth += atoi(digit_buf);
        } 
        else if (strncmp(line, "up", 2) == 0) {
            strncpy(digit_buf, line + 3, lend);
            depth -= atoi(digit_buf);
        }
        else
            printf("Unexpected op in line: `%s`\n", line);
    }
    printf("horizontal: %d depth: %d\n", horizontal, depth);

    fclose(fp);
    if (line)
        free(line);
    exit(EXIT_SUCCESS);
}