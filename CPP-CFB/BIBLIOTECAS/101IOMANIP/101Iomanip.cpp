#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    // setbase = base decimal, octal, hexadecimal
    cout << setbase(16);
    cout << 10 << "\n\n";
    cout << setbase(10);

    // setw = Largura do campo
    cout << setw(20);
    cout << "CFB";
    cout << setw(10);
    cout << "Cursos";
    cout << setw(40);
    cout << "Curso de C++" << "\n\n";

    // setfill = Preenchimento do campo
    cout << "Canal:" << setw(20) << setfill('.') << "CFB Cursos" << "\n\n";

    // setprecision = Precisão dos valores float e double, casas decimais
    double pi = 3.14159;
    cout << setprecision(3) << pi << "\n\n";

    return 0;
}