#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
    // calloc  malloc  ALOCAR MEMÓRIA
    // free  LIBERAR MEMÓRIA ALOCADA
    // realoc  AUMENTAR OU DIMINUIR MEMÓRIA ALOCADA

    int tam = 10, num;
    int *vetor;

    // vetor = (int *)calloc(tam, sizeof(int));
    vetor = (int *)malloc(sizeof(int));

    srand(time(NULL));

    for (int i = 0; i < tam; i++)
    {
        vetor[i] = rand() % 100;
        cout << vetor[i] << endl;
    }
    free(vetor);

    return 0;
}

/*
    double num;
    char numero[80];
    cin >> numero;
    //num = atof(numero);
    num = strtod(numero,NULL);
    cout << num << endl;
    //atof  atoi  altol  atoll(C++11)
    //astrtod  astrtof  astrtol  astrtoll
*/

/*
srand(time(NULL));
    for (int i = 0; i < 10; i++)
    {
        cout << rand() % 100 << endl;
    }
*/