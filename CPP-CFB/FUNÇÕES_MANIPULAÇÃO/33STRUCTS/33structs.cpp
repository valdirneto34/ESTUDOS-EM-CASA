#include <iostream>

using namespace std;

struct Carro
{
    string nome;
    string cor;
    int pot;
    int velMax;
};

int main()
{
    Carro car1, car2;

    car1.nome = "Tornado";
    car1.cor = "Vermelho";
    car1.pot = 450;
    car1.velMax = 350;

    car2.nome = "Luxo";
    car2.cor = "Preto";
    car2.pot = 250;
    car2.velMax = 260;

    cout << "Nome.............: " << car1.nome << endl;
    cout << "Cor..............: " << car1.cor << endl;
    cout << "Potencia.........: " << car1.pot << endl;
    cout << "Velocidade Maxima: " << car1.velMax << endl << endl;

    cout << "Nome.............: " << car2.nome << endl;
    cout << "Cor..............: " << car2.cor << endl;
    cout << "Potencia.........: " << car2.pot << endl;
    cout << "Velocidade Maxima: " << car2.velMax << endl;

    system("pause");
    return 0;
}
