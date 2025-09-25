#include <iostream>
#include <stdio.h>
#include <math.h>
#include <iomanip>

using namespace std;

int main()
{
    float pi = M_PI;
    printf("Valor de PI: %f\n", pi);
    printf("Valor de PI: %.2f\n", pi);
    int num = 5;
    printf("Valor de NUM: %d\n", num);
    printf("Valor de NUM: %07d\n", num);
    printf("Valor de PI: %07.1f\n\n", pi);

    int num2 = 15;
    cout << "Valor de NUM em dec: " << num2 << endl;
    cout << "Valor de NUM em hex: " << hex << num2 << endl; // HEXADECIMAL
    cout << "Valor de NUM em oct: " << oct << num2 << "\n\n"; // OCTAL

    int num3 = 10;
    cout << "Valor de NUM em dec: " << setbase(10) << num3 << endl;
    cout << "Valor de NUM em oct: " << setbase(8) << num3 << endl;
    cout << "Valor de NUM em hex: " << setbase(16) << num3 << "\n\n";

    cout.precision(3);
    cout << "Valor de PI: " << pi << endl;
    cout.precision(30);
    cout << "Valor de PI: " << pi << endl;
    cout.precision(-1);
    cout << "Valor de PI: " << pi << endl;
    cout << "Valor de PI: " << std::scientific << pi << "\n\n";

    int num4 = 30;
    cout << "Valor de NUM: " << setbase(10) << num4 << endl;
    cout << "Valor de NUM: " << setw(10) << num4 << endl;
    cout << "Valor de NUM: " << setw(10) << setfill('0') << num4 << endl;
    cout << "Valor de NUM: " << setw(10) << setfill('x') << num4 << endl;

    return 0;
}