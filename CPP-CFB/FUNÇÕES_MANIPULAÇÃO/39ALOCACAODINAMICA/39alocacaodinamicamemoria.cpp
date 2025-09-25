#include <iostream>
#include <stdio.h>  //Para função gets
#include <stdlib.h> //Para função malloc

using namespace std;
int main()
{
    char *vnome;
    vnome = (char *)malloc(sizeof(char) + 1);
    cout << "Digite seu nome: ";
    gets(vnome);
    cout << "Seu nome: " << vnome;
    free(vnome);
    return 0;
}
