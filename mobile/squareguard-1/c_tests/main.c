#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define PASSWORD_LENGTH 6



long hex_to_num(char *param_1){
    int local_28;
    unsigned char local_21;
    long local_20;
    unsigned char *local_18;

    local_20 = 0;
    local_18 = (unsigned char *)param_1;
    do {
        if (*local_18 == 0) {
            return local_20;
        }
        local_21 = *local_18;
        if (('`' < (char)local_21) && ((char)local_21 < '{')) {
            local_21 = local_21 & 0xdf;
        }
        if (((char)local_21 < '0') || ('9' < (char)local_21)) {
        if (((char)local_21 < 'A') || ('F' < (char)local_21)) {
            return -1;
        }
            local_28 = (char)local_21 + -0x37;
        }
        else {
            local_28 = (char)local_21 + -0x30;
        }
        local_20 = local_20 * 0x10 + (long)local_28;
        local_18 = local_18 + 1;
    } while( 1 );
}

int extractKey(char *password){
    int key_part_one;
    int key_part_2;
    int key_part_3;

    password[6] = '\0';
    key_part_one = hex_to_num(password);
    //
    if (((key_part_one >> 0x10) % 0x100 ^ (key_part_one >> 8) % 0x100) == key_part_one % 0x100) {
        password[0xd] = '\0';
        printf("First key okay");
        key_part_2 = hex_to_num(password + 7);
        if (((key_part_2 >> 0x10) % 0x100 ^ (key_part_2 >> 8) % 0x100) == key_part_2 % 0x100) {
            password[0x14] = '\0';
            hex_to_num(password);
            key_part_3 = ((key_part_one >> 8) % 0x10000) * 0x10000 + (key_part_2 >> 8) % 0x10000;
        }
        else {
            key_part_3 = -1;
        }
    }
    else {
        key_part_3 = -1;
    }
    return key_part_3;
}

int main(){
    // char password[] = "000000000000";
    // password = 0x123456;
    // int key = extractKey(password);
    // if (key != -1){
    //     printf("Key: %d", key);
    // }
    // else{
    //     printf("Invalid password\n");
    // }

    char password[PASSWORD_LENGTH + 1]; // Add 1 for null terminator
    memset(password, '0', PASSWORD_LENGTH); // Initialize password to all '0's
    password[PASSWORD_LENGTH] = '\0'; // Add null terminator

    while (1) { // Loop infinitely until break
        // Increment password
        // int i = PASSWORD_LENGTH - 1;
        // while (password[i] == 'F') {
        //     password[i] = '0';
        //     i--;
        // }
        // if (i < 0) { // Password has overflowed
        //     break;
        // }
        // password[i]++; // Increment digit at position i
        // int pch = strstr(password, "?") || strstr(password, "@") || strstr(password, ":");
        // pch = pch || strstr(password, ";") || strstr(password, "<") || strstr(password, "=") || strstr(password, ">");
        // if(pch){
        //     continue;
        // }

        FILE* fptr_1 = fopen("key_1.txt", "r"); 

        // Store the content of the file

        char key_part_1[7];
        char key_part_2[7];

        unsigned int local_6c;
        char *result;
        int extracted_key;
        char *local_38;
        char *local_30;
        char *local_28;
        char *local_20;
        unsigned char bVar1;

        // while(fgets(key_part_1, 7, fptr_2)){
        //     printf("%s", key_part_1);
        // }

        while(fgets(key_part_1, 6, fptr_1)){
            FILE* fptr_2 = fopen("key_2.txt", "r"); 
            while(fgets(key_part_2, 6, fptr_2)){
                printf("Bef init\n");
                int key_part_1_int = hex_to_num(key_part_1);
                int key_part_2_int = hex_to_num(key_part_2);
                int extracted_key = ((key_part_1_int >> 8) % 0x10000) * 0x10000 + (key_part_2_int >> 8) % 0x10000;
                printf("Bef if\n");

                if (extracted_key == -1) {
                    continue;
                } else {
                    local_38 = (char *)0x675c417c49595070;
                    local_30 = (char *)0x6d544c7a665b4060;
                    local_28 = (char *)0x7c4f4c756d4e4c7d;
                    // local_20._0_2_ = 0x7e77;
                    // local_20._2_1_ = 0x1a;
                    local_6c = 0;
                    while( 1 ) {
                        printf("Start loop\n");
                        unsigned char* local_ptr = (unsigned char*)(&local_38 + local_6c);
                        unsigned char* key_ptr = (unsigned char*)(&extracted_key + (local_6c % 4));
                        bVar1 = (*local_ptr) ^ (*key_ptr);
                        printf("Middle loop\n");
                        *(unsigned char *)((long)&local_38 + (long)(int)local_6c) = bVar1;
                        if ((bVar1 == 0) || (0x1a < local_6c)) break;
                        local_6c = local_6c + 1;
                        printf("End loop\n");
                    }
                    printf("Out loop\n");
                    if ((strcmp(local_38[0], 'C') == 0 && (local_38[1] == 'S') && (local_38[2] == 'C') && (local_38[3] == '{')) {
                        printf("FLAG: %s\n", local_38);
                        return 0;
                    }
                    printf("End\n");
                }
            }
            fclose(fptr_2);
        }

    }

    return 0;
}
