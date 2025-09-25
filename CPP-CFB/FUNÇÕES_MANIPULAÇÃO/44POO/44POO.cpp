#include <iostream>

using namespace std;

class Aviao
{
public:
    int vel = 0;
    int velMax;
    string tipo;
    void ini(int tp);

private:
};

void Aviao::ini(int tp)
{
    if (tp == 1)
    {
        this->velMax = 800;
        this->tipo = "Jato";
    }
    else if (tp == 2)
    {
        this->velMax = 350;
        this->tipo = "Monomotor";
    }
    else if (tp == 3)
    {
        this->velMax = 180;
        this->tipo = "Planador";
    }
}

int main()
{
    Aviao *av1 = new Aviao();
    av1->ini(1);
    cout << "Velocidade.......: " << av1->vel << endl;
    cout << "Velocidade Maxima: " << av1->velMax << endl;
    cout << "Tipo.............: " << av1->tipo << "\n\n";

    Aviao *av2 = new Aviao();
    av2->ini(2);
    cout << "Velocidade.......: " << av2->vel << endl;
    cout << "Velocidade Maxima: " << av2->velMax << endl;
    cout << "Tipo.............: " << av2->tipo << "\n\n";

    Aviao *av3 = new Aviao();
    av3->ini(3);
    cout << "Velocidade.......: " << av3->vel << endl;
    cout << "Velocidade Maxima: " << av3->velMax << endl;
    cout << "Tipo.............: " << av3->tipo << "\n\n";

    return 0;
}