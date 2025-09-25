#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool menor50(int i)
{
    return i < 50;
}

int main()
{
    vector<int> vt = {2, 4, 12, 7, 8, 10, 12, -8, 1, 3, 5, 6, 9, 11, 13, 2, 7, 2};
    for (auto x : vt)
        cout << x << "  ";
    cout << "\n\n";
    // all_of = Retorna true se o teste retornar true com todos os elementos da coleção
    if (all_of(vt.begin(), vt.end(), menor50))
        cout << "Todos sao menores que 50" << "\n\n";
    else
        cout << "Existe um ou mais elementos maiores que 50" << "\n\n";

    // any_of = Retorna true se o teste retornar true pelo menos com um dos elementos da coleção
    if (any_of(vt.begin(), vt.end(), [](int i)
               { return i > 12; }))
        cout << "Existe um ou mais elementos maiores que 12" << "\n\n";
    else
        cout << "Todos sao menores ou iguais a 12" << "\n\n";

    // none_of = Retorna false se o teste retornar false pelo menos com um dos elementos da coleção
    if (none_of(vt.begin(), vt.end(), [](int i)
                { return i < 0; }))
        cout << "Todos sao positivos" << "\n\n";
    else
        cout << "Existe um negativo" << "\n\n";

    // for_each = Aplica uma função a todos os elementos da coleção
    cout << "Dobro" << endl;
    for_each(vt.begin(), vt.end(), [](int i)
             { cout << i * 2 << "  "; });
    cout << "\n\n";

    // find = Procura um elemento e retorn um iterator com o resultado
    auto it = find(vt.begin(), vt.end(), 12);
    cout << *it << endl;

    // find_if = Procura um elemento que atenda a uma determinada condição e retorna um iterator com o resultado
    auto it2 = find_if(vt.begin(), vt.end(), [](int i)
                       { return ((i % 2) == 1); });
    cout << "Primeiro elemento impar: " << *it2 << "\n\n";

    // find_if_not = Procura um elemento que NÃO atenda a uma determinada condição e retorna um iterator com o resultado
    auto it3 = find_if_not(vt.begin(), vt.end(), [](int i)
                           { return ((i % 2) == 1); });
    cout << "Primeiro elemento par: " << *it3 << "\n\n";

    // count = Qtde de um determinado elemento
    cout << "Quantidade do numeral 2: " << count(vt.begin(), vt.end(), 2) << "\n\n";

    // count_if = Qtde de um determinado elemento na coleção, que atenda a uma condição
    cout << "Quantidade de impares: " << count_if(vt.begin(), vt.end(), [](int i)
                                                { return ((i % 2) == 1); })
         << "\n\n";

    return 0;
}