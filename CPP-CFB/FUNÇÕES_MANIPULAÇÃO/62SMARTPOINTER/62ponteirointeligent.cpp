#include <iostream>
#include <memory>

class Carro
{
public:
    int vel = 0;
    int getVel()
    {
        return vel;
    }
    void setVel(int v)
    {
        this->vel = v;
    }
};

using namespace std;

int main()
{
    // unique_ptr<string> str(new string("CFB Cursos"));
    // cout << *str << " - tamanho: " << str->size() << endl;

    unique_ptr<Carro> c1(new Carro);
    unique_ptr<Carro> c2(new Carro);
    c1->setVel(10);
    c2->setVel(5);
    cout << "Velocidade: " << c1->getVel() << endl;
    cout << "Velocidade: " << c2->getVel() << endl;

    return 0;
}

/*// int *pnum = new int();
    // shared_ptr<int> pnum(new int());
    unique_ptr<int> pnum(new int());
    *pnum = 10;
    cout << *pnum << " - " << &pnum << endl;

    string* str=new string("CFB Cursos");
    cout << *str << " - tamanho: " << str->size() << endl;
    delete str;

    Carro *c1 = new Carro();
    cout << "Velocidade: " << c1->getVel() << endl;
    */