#include <iostream>
#include <typeinfo>

using namespace std;

class CFB
{
};

int main()
{
    if (typeid(int).before(typeid(char)))
        cout << "INT vem antes de CHAR." << endl;
    else
        cout << "CHAR vem antes de INT." << endl;

    if (typeid(int).before(typeid(double)))
        cout << "INT vem antes de DOUBLE." << endl;
    else
        cout << "DOUBLE vem antes de INT." << endl;

    return 0;
}

/*
    auto num{10.5};
    CFB cfb;
    cout << "Tipo de num: " << typeid(cfb).name() << endl;
*/