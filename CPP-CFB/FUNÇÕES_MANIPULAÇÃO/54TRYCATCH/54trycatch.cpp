#include <iostream>
#include <vector>
#include <stdexcept>

double divide(double n10, double n20);

using namespace std;

int main()
{
    /*vector<int> num(5); // 0 1 2 3 4
    try
    {
        num.at(5) = 10;
        cout << num[5] << endl;
    }
    catch (exception &e)
    {
        cout << "ERRO: " << e.what() << '\n';
    }*/

    double n1, n2;
    cin >> n1 >> n2;

    try
    {
        cout << divide(n1, n2) << endl;
    }
    catch (const char* msg)
    {
        cout << "ERRO: " << msg << endl;
    }

    return 0;
}

double divide(double n10, double n20)
{
    if (n20 == 0)
    {
        throw "Erro de divisao por ZERO.";
    }
    if(n10 >= 10){
        throw "N1 precisa ser menor que 10.";
    }
    return n10 / n20;
}