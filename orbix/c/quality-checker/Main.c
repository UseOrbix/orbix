#include <stdio.h>

int main(int argc, char *argv[]) {
    if(argc < 2) {
        printf("Usage: %s <file.c>\n", argv[0]);
        return 1;
    }
    FILE *file = fopen(argv[1], "r");
    char line[1024];
    int line_num = 0;
    while(fgets(line, sizeof(line), file)) {
        line_num++;
        if(strlen(line) > 80)
            printf("Line %d exceeds 80 characters.\n", line_num);
    }
    fclose(file);
    return 0;
}
