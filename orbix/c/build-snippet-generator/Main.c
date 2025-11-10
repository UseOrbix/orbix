#include <stdio.h>

int main() {
    FILE *file = fopen("Makefile", "w");
    fprintf(file, "all:\n\tgcc main.c -o main\n");
    fclose(file);
    printf("Makefile created.\n");
    return 0;
}
