#include <iostream>
#include <memory>

class Carro
{
public:
    const char *nome;
    int velMax;
    int potencia;
    // Lista de inicialização
    Carro(const char *n, int p) : nome(n), potencia(p)
    {
        if (p < 100)
            this->velMax = 120;
        else if (p < 200)
            this->velMax = 220;
        else
            this->velMax = 350;
    }
};

using namespace std;

int main()
{
    unique_ptr<Carro> c1(new Carro{"Bruno", 85});
    cout << c1->nome << " - " << c1->potencia << " - " << c1->velMax << endl;

    Carro c2{"Ventania", 400};
    cout << c2.nome << " - " << c2.potencia << " - " << c2.velMax << endl;

    return 0;
}
