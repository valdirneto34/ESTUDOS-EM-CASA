#include <iostream>
#include <cstdlib>

using namespace std;

int comparacao(const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
    // 0 -> a = b
    //>0 -> a > b
    //<0 -> a < b
}

int main()
{
    int vetor[] = {9, 1, 8, 2, 7, 3, 6, 4, 5, 0};
    int pesq = 7;
    int *pos;

    qsort(vetor, 10, sizeof(int), comparacao);
    for (size_t i = 0; i < 10; i++)
    {
        cout << vetor[i] << endl;
    }

    pos = (int *)bsearch(&pesq, vetor, 10, sizeof(int), comparacao);

    cout << "Elemento " << pesq << " esta na posicao " << *pos << endl;

    return 0;
}

/*
    void fim()
    {
        cout << "CFB Cursos" << endl;
    }
    atexit(fim);
    // at_quick_exit(fim); //C++11
    for (int i = 0; i < 10; i++)
    {
        if (i < 5)
        {
            cout << i << endl;
        }
        else
        {
            // exit(EXIT_SUCCESS);
            // quick_exit(EXIT_SUCCESS); // C++11
            cout << i << endl;
        }
    }
*/

/*
const char *p;
p = getenv("PATH");
cout << p << endl;
*/

/*
const char *canal = "CFB Cursos";
    for (size_t i = 0; i < 10; i++)
    {
        cout << i << endl;
    }
    _Exit(EXIT_SUCCESS); // C++11
    system("cls");
    system("dir");
    cout << canal << endl;
    system("Pause");
*/