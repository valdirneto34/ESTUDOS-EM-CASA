#include <iostream>
#include <vector>

using namespace std;

auto soma(double n1, double n2) -> int
{
    return n1 + n2;
};

string canal()
{
    return "CFB Cursos";
};

void somador()
{
    static auto i = 0;
    i++;
    cout << i << endl;
};

int main()
{
    register int cont;
    for (cont = 0; cont <= 10; cont++)
    {
        cout << cont << endl;
    }
    auto num = 10;
    auto nome = "Bruno";
    auto valor = 10.5;
    auto res = soma(10.3, 5.2);
    vector<int> v{10, 20, 30, 40, 50, 60, 70};
    cout << endl;
    for (auto it = v.begin(); it != v.end(); it++)
    {
        cout << *it << endl;
    }
    cout << "\nRes: " << res << "\n\n";
    somador();
    somador();
    somador();
    somador();
    somador();
    somador();

    return 0;
}