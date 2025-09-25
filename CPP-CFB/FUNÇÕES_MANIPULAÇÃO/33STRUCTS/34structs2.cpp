#include <iostream>

using namespace std;

struct Carro
{
    string nome;
    string cor;
    int pot;
    int velMax;
    int vel;

    void insere(string stnome, string stcor, int stpot, int stvelMax)
    {
        nome = stnome;
        cor = stcor;
        pot = stpot;
        velMax = stvelMax;
        vel = 0;
    }

    void mostra()
    {
        cout << "Nome.............: " << nome << endl;
        cout << "Cor..............: " << cor << endl;
        cout << "Potencia.........: " << pot << endl;
        cout << "Velocidade atual.: " << vel << endl;
        cout << "Velocidade Maxima: " << velMax << "\n\n";
    }

    void mudaVel(int mv)
    {
        vel = mv;
        if (vel > velMax)
        {
            vel = velMax;
        }
        if (vel < 0)
        {
            vel = 0;
        }
    }
};

int main()
{
    Carro car1, car2, car3, car4;

    car1.insere("Tornado", "Vermelho", 450, 350);
    car2.insere("Luxo", "Preto", 250, 260);

    car1.mostra();
    car1.mudaVel(150);
    car1.mostra();
    car1.mudaVel(400);
    car1.mostra();

    car2.mostra();

    system("pause");
    return 0;
}
