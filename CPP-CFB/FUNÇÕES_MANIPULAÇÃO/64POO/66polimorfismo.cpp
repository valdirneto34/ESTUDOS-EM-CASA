#include <iostream>

class Carro
{
private:
    int velMax;
    const char *nome;

public:
    int potencia;
    int getVelMax()
    {
        return velMax;
    }
    const char *getNome()
    {
        return nome;
    }
    Carro() // Sobrecarga de métodos
    {
        velMax = 120;
        potencia = 85;
        nome = "Popular";
    }
    Carro(const char *no, int pt) : nome(no), potencia(pt)
    {
        if (pt < 100)
            velMax = 120;
        else if (pt < 200)
            velMax = 200;
        else
            velMax = 350;
    }
    // Fim sobrecarga
};

using namespace std;

int main()
{
    Carro c1;
    cout << c1.getNome() << " - " << c1.potencia << " - " << c1.getVelMax() << endl;

    Carro c2{"Luxo", 180};
    cout << c2.getNome() << " - " << c2.potencia << " - " << c2.getVelMax() << endl;

    Carro c3{"Esportivo", 300};
    cout << c3.getNome() << " - " << c3.potencia << " - " << c3.getVelMax() << endl;

    return 0;
}