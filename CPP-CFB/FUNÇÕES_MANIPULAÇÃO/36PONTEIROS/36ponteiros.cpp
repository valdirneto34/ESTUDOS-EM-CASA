#include <iostream>
#include <windows.h>   // Biblioteca para acentuação

using namespace std;

int main()
{
    SetConsoleOutputCP(CP_UTF8);   //Só funciona em Windows
    string veiculo = "Carro";
    string *pv;

    pv = &veiculo;     // Ponteiro PV recebe o endereço da variavel veiculo

    cout << pv << endl << &veiculo << endl;

    *pv = "Moto";     // No endereco apontado por ponteiro *pv adicione o valor "Moto"

    cout << veiculo << endl << *pv << endl;

    return 0;
}