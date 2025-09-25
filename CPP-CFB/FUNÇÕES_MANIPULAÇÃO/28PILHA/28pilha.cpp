#include <iostream>
#include <stack>

using namespace std;

int main()
{
    stack<string> cartas;
    cartas.push("Rei de Copas");
    cartas.push("Rei de Espadas");
    cartas.push("Rei de Ouros");
    cartas.push("Rei de Paus");
    if (cartas.empty())
    {
        cout << "Pilha de cartas vazia." << endl;
    }
    else
    {
        cout << "Pilha com " << cartas.size() << " cartas no momento." << endl;
    }
    cout << "Carta do topo: " << cartas.top() << endl;
    cartas.pop();
    cout << "Nova carta do topo: " << cartas.top() << endl;
    cartas.pop();
    cout << "Nova carta do topo: " << cartas.top() << endl;
    if (cartas.empty())
    {
        cout << "Pilha de cartas vazia." << endl;
    }
    else
    {
        cout << "Pilha com " << cartas.size() << " cartas no momento." << endl;
    }
    while (!cartas.empty())
    {
        cout << "Carta do topo: " << cartas.top() << endl;
        cartas.pop();
        if (cartas.empty())
        {
            cout << "Pilha de cartas vazia!" << endl;
        }
    }
    /*
    push();
    pop();
    top();
    size();
    empty();
    */
    system("pause");
    return 0;
}