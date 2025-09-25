#include <iostream>

using namespace std;

int main()
{
    int *p;
    int vetor[10];

    p = &vetor[0]; // p = vetor;
    *p = 10; // vetor[0] = 10;
    cout << vetor[0] << "\n";

    *(p += 1);
    *p = 20;; // vetor[1] = 20;
    cout << vetor[1] << "\n";

    *(p += 1);
    *p = 30;; // vetor[2] = 30;
    cout << vetor[2] << "\n";

    *(p += 1);
    cout << p << "\n";

    return 0;
}