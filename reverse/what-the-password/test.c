#include <stdio.h>

char pwd[] = {'l', '3', 't', 'm', '3', '1', 'n', '\x00'};
char flag[] = "csc{n0t_wh4t_1t_s33ms!}";

void __construct_gc(void){
    unsigned char bVar1;
    int iVar2;

    long int local_48;
    long int local_40;
    long int local_38;
    long int local_28;

    int index_2;
    int index;

    local_28 = 0x7701452a434b3c;
    for (index = 0; index < 8; index = index + 1) {
        iVar2 = ((int)pwd[index] - (int)*(char *)((long)&local_28 + (long)index)) + 0x80;
        // Print the result of the operation
        printf("index: %2d ", index);
        printf("ivar2: %3d ", iVar2);
        bVar1 = (iVar2 >> 0x1f);
        // Print the result of the operation
        printf("bvar1: %3d ", bVar1);
        pwd[index] = ((char)iVar2 + (bVar1 >> 1) & 0x7f) - (bVar1 >> 1);
        printf("pwd[%d]: %c\n", index, pwd[index]);
    }

    local_48 = 0x154137186b404877;
    local_40 = 0x67f46146c43496b;
    local_38 = 0x3e42;

    for (index_2 = 0; index_2 < 20; index_2 = index_2 + 1) {
        iVar2 = ((int)flag[index_2 + 4] - (int)*(char *)((long)&local_48 + (long)index_2)) + 0x80;
        bVar1 = (iVar2 >> 0x1f);
        printf("index: %2d ", index_2);
        printf("ivar2: %3d ", iVar2);
        printf("bvar1: %3d ", bVar1);
        flag[index_2 + 4] = ((char)iVar2 + (bVar1 >> 1) & 0x7f) - (bVar1 >> 1);
        printf("flag[%2d]: %c\n", index_2 + 4, flag[index_2 + 4]);
    }
    printf("pwd: %s\n", pwd);
    printf("flag: %s\n", flag);
    return;
}

int main(void){
    __construct_gc();
    return 0;
}
