#include <string>
#ifndef CLASSES_H_INCLUDED
#define CLASSES_H_INCLUDED

using namespace std;

class Veiculo
{
public:
    int vel;
    int tipo;
    Veiculo(int tp);
    int getVelMax();
    bool getLigado();
    void setLigado(int l);
    string getNome();

private:
    void setVelMax(int vm);
    string nome;
    int velMax;
    bool ligado;
};

// Criado por mim-----------------------------
string Veiculo::getNome()
{
    return nome;
}
//---------------------------------------------

bool Veiculo::getLigado()
{
    return ligado;
}

void Veiculo::setLigado(int l)
{
    if (l == 1)
    {
        ligado = true;
    }
    else if (l == 0)
    {
        ligado = false;
    }
}

int Veiculo::getVelMax()
{
    return velMax;
}

void Veiculo::setVelMax(int vm)
{
    velMax = vm;
}

Veiculo::Veiculo(int tp) // 1=Carro, 2=Aviao, 3=Navio
{
    if (tipo == 1)
    {
        nome = "Carro";
        setVelMax(200);
    }
    else if (tipo == 2)
    {
        nome = "Aviao";
        setVelMax(800);
    }
    else if (tipo == 3)
    {
        nome = "Navio";
        setVelMax(120);
    }
    setLigado(0); // ligado = false;
}

#endif // CLASSES_H_INCLUDED