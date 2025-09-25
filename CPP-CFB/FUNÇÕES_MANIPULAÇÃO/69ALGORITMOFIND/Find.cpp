#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <string>

using namespace std;

int main()
{
    string texto = "CFB Cursos - Aula de C++";
    size_t enc = texto.find("Chip");
    if (enc != string::npos)
        cout << "Palavra encontrada: " << enc << endl;
    else
        cout << "Palavra NAO encontrada!" << endl;

    return 0;
}
/*
int vetor[] = {5, 3, 1, 4, 7, 2, 6};
    int *p;
    size_t tam = sizeof vetor / 4;
    p = find(vetor, vetor + tam, 16);
    if (p != vetor + tam)
        cout << "Numeral encontrado: " << *p << endl;
    else
        cout << "Numeral NAO encontrado!" << endl;

    vector<int> num = {5, 3, 1, 4, 7, 2, 6};
    auto it = find(num.begin(), num.end(), 7);
    if (it != num.end())
        cout << "Numeral encontrado: " << *it << endl;
    else
        cout << "Numeral NAO encontrado!" << endl;

    list<int> nums = {5, 3, 1, 4, 7, 2, 6};
    auto ite = find(nums.begin(), nums.end(), 17);
    if (ite != nums.end())
        cout << "Numeral encontrado: " << *ite << endl;
    else
        cout << "Numeral NAO encontrado!" << endl;
*/

/*
vector<int> numeros;
    vector<int>::iterator it;
    int num, qtde = 10;

    while (qtde > 0)
    {
        cout << "Digite um numeral: ";
        cin >> num;
        it = find(numeros.begin(), numeros.end(), num);
        if (it != numeros.end())
            cout << "Numeral ja existe no vector!" << endl;
        else
        {
            numeros.push_back(num);
            qtde--;
        }
    }
*/

/*
map<char, int> mapa;
    mapa['a'] = 10;
    mapa['b'] = 33;
    mapa['c'] = 25;
    mapa['e'] = 5;
    mapa['d'] = 80;

    auto it = mapa.find('f');
    int num, qtde = 10;

    if (it != mapa.end())
    {
        cout << "Chave encontrada: " << it->second << endl;
    }
    else
    {
        cout << "Chave NAO encontrada!" << endl;
    }
*/