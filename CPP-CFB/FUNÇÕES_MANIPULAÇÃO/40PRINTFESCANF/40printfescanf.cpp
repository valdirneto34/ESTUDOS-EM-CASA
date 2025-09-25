#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    printf("Canal Fessor Bruno\nCurso de C++\n");
    char nome[10]="Bruno";
    int num1, num2, num3, num4, ano;
    num1 = 1;
    num2 = 2;
    num3 = 3;
    printf("Valor das variaveis: %d %d %d\n", num1, num2, num3);
    printf("Nome: %s\n", nome);
    cout << "Digite NUM4: ";
    scanf("%i", &num4);
    printf("Valor de NUM4: %i\n\n", num4);
    printf("Informe o ano de seu nascimento: ");
    scanf("%d", &ano);
    printf("\nNome: %s - Ano de nascimento: %d\n\n", nome, ano);

    return 0;
}

/*
d, i => int
x, X => Hexadecimal
u => int sem sinal
s => string, char*
f => double
p => ponteiros
*/
