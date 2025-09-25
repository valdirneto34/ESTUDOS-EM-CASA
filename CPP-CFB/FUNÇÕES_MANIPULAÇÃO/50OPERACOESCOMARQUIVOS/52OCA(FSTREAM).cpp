#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main()
{
    // oftream, ifstream, fstream

    fstream arquivo;
    char opc = 's';
    string nome, linha;

    arquivo.open("cfbcursos3.txt", ios::out | ios::app);

    while (opc == 's' || opc == 'S')
    {
        cout << "Digite um nome: ";
        cin >> nome;
        arquivo << nome << "\n";
        cout << "\nDigitar um novo nome? [S/N] ";
        cin >> opc;
        system("cls");
    }
    arquivo.close();

    arquivo.open("cfbcursos3.txt", ios::in);

    cout << "---------Nomes Digitados---------" << endl;
    if (arquivo.is_open())
    {
        while (getline(arquivo, linha))
        {
            cout << linha << endl;
        }
        arquivo.close();
    }
    else
    {
        cout << "Nao foi possivel abrir o arquivo!" << endl;
    }
    cout << "---------------------------------" << endl;

    return 0;
}