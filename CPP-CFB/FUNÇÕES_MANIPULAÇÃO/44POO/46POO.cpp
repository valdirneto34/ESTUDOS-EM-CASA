#include <iostream>
#include "classes.h"

using namespace std;

int main()
{
    Veiculo *v1 = new Veiculo(1);
    Veiculo *v2 = new Veiculo(2);
    Veiculo *v3 = new Veiculo(3);

    //v1->setLigado(0);
    v2->setLigado(1);
    //v3->setLigado(0);

    cout << "VelMax 1: " << v1->getVelMax() << endl;
    cout << "VelMax 2: " << v2->getVelMax() << endl;
    cout << "VelMax 3: " << v3->getVelMax() << endl;

    if (v1->getLigado())
    {
        cout << "Veiculo 1 esta ligado." << endl;
    }
    else
    {
        cout << "Veiculo 1 esta desligado." << endl;
    }
    if (v2->getLigado())
    {
        cout << "Veiculo 2 esta ligado." << endl;
    }
    else
    {
        cout << "Veiculo 2 esta desligado." << endl;
    }
    if (v3->getLigado())
    {
        cout << "Veiculo 3 esta ligado." << endl;
    }
    else
    {
        cout << "Veiculo 3 esta desligado." << endl;
    }

    cout << "Nome v1: " << v1->getNome() << endl;
    cout << "Nome v2: " << v2->getNome() << endl;
    cout << "Nome v3: " << v3->getNome() << endl;

    delete v1, v2, v3;

    return 0;
}