#include <iostream>
#include <list>

using namespace std;

int main()
{
    list<int> aula, teste;
    int tam;
    list<int>::iterator it;

    teste.push_front(9);
    teste.push_front(9);
    teste.push_front(9);
    teste.push_front(9);

    tam = 10;

    for (int i = 0; i < tam; i++)
    {
        aula.push_front(i);
    }

    it = aula.begin();
    advance(it, 3);
    aula.insert(it, 0);
    aula.erase(--it);

    // aula.clear(); REMOVE TODOS OS ELEMENTOS DA LISTA
    // REMOVE OS ELEMENTOS DA LISTA TESTE E INSERE NA LISTA AULA->
    aula.merge(teste);

    cout << "Tamanho da lista: " << aula.size() << endl;

    tam = aula.size();
    for (int i = 0; i < tam; i++)
    {
        cout << aula.front() << endl;
        aula.pop_front();
    }

    cout << "Tamanho da lista: " << aula.size() << endl;

    system("pause");
    return 0;
}