#include <iostream>
#include <vector>
#include <map>

using namespace std;

struct Pessoa
{
    string nome;
    int idade;
};

class Veiculo
{
public:
    int tipo;
    string nome;
};

int main()
{
    int vetor[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int num{10};
    string nome{"CFB"};
    vector<int> valores{1, 2, 3, 4, 5};
    map<string, string> capitais{{"MG", "Belo Horizonte"}};
    Pessoa p1{"Valdir", 20};
    Pessoa p2{"Juliana", 42};
    Veiculo v1{1, "Carango"};

    cout << "Vetor: ";
    for (int i = 0; i < 10; i++)
    {
        cout << vetor[i] << " ";
    }
    cout << "\nNum: " << num << endl;
    cout << "Nome: " << nome << endl;
    for (vector<int>::iterator it = valores.begin(); it != valores.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
    for (map<string, string>::iterator it = capitais.begin(); it != capitais.end(); it++)
    {
        cout << it->first << " - " << it->second << endl;
    }
    cout << p1.nome << " - " << p1.idade << endl;
    cout << p2.nome << " - " << p2.idade << endl;
    cout << v1.tipo << " - " << v1.nome << endl;

    return 0;
}