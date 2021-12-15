#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

#define MAX_ARGS_LEN 100

int main(int argc, char **argv)
{
    printf(argv[0]);
    printf("\n");
    printf(argv[1]);
    printf("\n");
    if (argc != 2) {
        perror("wrong arguments\n");
        exit(0);
    }

    char* app_name = argv[1];
    char* str = malloc(100*sizeof(char));

    char cwd[100];
    if (getcwd(cwd, sizeof(cwd)) != NULL) {
    }

    sprintf(str, "%s/sys/bin/%s", cwd, app_name);

    system(str);

    return 0;
}