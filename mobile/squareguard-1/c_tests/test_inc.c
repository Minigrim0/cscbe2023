#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define PASSWORD_LENGTH 6

int main() {
    char password[PASSWORD_LENGTH + 1]; // Add 1 for null terminator
    memset(password, '0', PASSWORD_LENGTH); // Initialize password to all '0's
    password[PASSWORD_LENGTH] = '\0'; // Add null terminator
    
    while (1) { // Loop infinitely until break
        printf("%s\n", password); // Print password

        // Increment password
        int i = PASSWORD_LENGTH - 1;
        while (password[i] == 'F') {
            password[i] = '0';
            i--;
        }
        if (i < 0) { // Password has overflowed
            break;
        }
        password[i]++; // Increment digit at position i
    }
    
    return 0;
}
