#include <iostream>
#include <queue>

using namespace std;

int main()
{
    queue<string> cartas;
    cartas.push("Rei de Copas");
    cartas.push("Rei de Espadas");
    cartas.push("Rei de Ouros");
    cartas.push("Rei de Paus");
    cout << "Tamanho da fila: " << cartas.size() << endl;
    cout << "Primeira carta: " << cartas.front() << endl;
    cout << "Ultima carta: " << cartas.back() << endl;

    while (!cartas.empty())
    {
        cout << "Primeira carta: " << cartas.front() << endl;
        cartas.pop();
    }

    /*
    cartas.front();
    cartas.back();
    cartas.empty();
    cartas.size();
    cartas.push();
    */

    system("pause");
    return 0;
}