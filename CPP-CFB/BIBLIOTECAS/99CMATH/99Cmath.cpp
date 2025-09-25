#include <iostream>
#include <cmath> // math.h

#define PI 3.14159265

double radToGra(int a)
{
    return a * PI / 180;
}

using namespace std;

int main()
{
    // Sin, Cos, Tan = Seno, Cosseno, Tangente
    int ang = 45;
    cout << "Seno de " << ang << "....: " << sin(ang * PI / 180) << endl;
    cout << "Cosseno de " << ang << ".: " << cos(ang * PI / 180) << endl;
    cout << "Tangente de " << ang << ": " << tan(ang * PI / 180) << endl;
    cout << endl;

    // asin, acos, atan = Arco seno, Arco cosseno, Arco tangente
    printf("Arco Seno de %d....: %f\n", ang, asin(radToGra(ang)));
    printf("Arco Cosseno de %d.: %f\n", ang, acos(radToGra(ang)));
    printf("Arco Tangente de %d: %f\n\n", ang, atan(radToGra(ang)));

    // atan2 = Calcula o arco tangente usando dois parâmetros representados de x e y
    double x = -10.0, y = 10.0;
    cout << "arco Tangente de X=-10 e Y=10: " << atan2(x, y) * 180 / PI << "\n\n";

    // exp = Função exponencial
    double x2 = 10;
    cout << "O valor exponencial de " << x2 << ": " << exp(x2) << "\n\n";

    // log = Retorna o Logaritmop natural de um número
    double x3 = 10;
    cout << "Logaritmo natural de " << x3 << ": " << log(x3) << "\n\n";

    // pow = Calcula a potência de um número base elevado a um expoente
    double x4 = 10;
    cout << "10 elevado a 2: " << pow(x4, 2) << "\n\n";

    // sqrt = Calcula a raiz quadrada de um número
    double x5 = 9;
    cout << "Raiz quadrada de 9: " << sqrt(x5) << "\n\n";

    // Cbrt (C++11) = Calcula a raiz cúbica dd um número
    double x6 = 27;
    cout << "Raiz cubica de 27: " << cbrt(x6) << "\n\n";

    // hypot (C++11) = Retorna a hipotenusa(lado maior de um triângulo retângulo)
    double cat1 = 3, cat2 = 4;
    cout << "Catetos: " << cat1 << ", " << cat2 << ", Hipotenusa: " << hypot(cat1, cat2) << endl;
    // O quadrado da hipotenusa é igual a soma do quadrado dos catetos
    cout << "Catetos: " << cat1 << ", " << cat2 << ", Hipotenusa: " << sqrt(pow(cat2, 2) + pow(cat1, 2)) << "\n\n";

    // ceil = Arredonda para cima retornando o numeral inteiro mais próximo
    double a = 2.2, b = 3.8, c = -2.7, d = -1.2;
    cout << a << " = " << ceil(a) << "\n";
    cout << b << " = " << ceil(b) << "\n";
    cout << c << " = " << ceil(c) << "\n";
    cout << d << " = " << ceil(d) << "\n\n";
    // floor = Arredonda para baixo retornando o numeral inteiro mais próximo
    cout << a << " = " << floor(a) << "\n";
    cout << b << " = " << floor(b) << "\n";
    cout << c << " = " << floor(c) << "\n";
    cout << d << " = " << floor(d) << "\n\n";

    // fmod = Retorna o resto de divisão (float)
    double e = 5.7, f = 2;
    cout << fmod(e, f) << "\n\n";

    // round = Arredonda para baixo ou para cima, conforme a regra padrão
    double g = 5.6, h = 5.4;
    cout << round(g) << endl;
    cout << round(h) << endl;
    cout << rint(g) << endl;
    cout << rint(h) << "\n\n";

    // fdim (C++11) = Retorna a diferença (positivo) entre dois números
    double i = 15, j = 9;
    cout << fdim(i, j) << "\n\n";

    // fmax (C++11) = Retorna o maior valor dentre dois
    // fmin (C++11) = Retorna o menor valor dentre dois
    double k = 15, l = 9;
    cout << fmax(k, l) << endl;
    cout << fmin(k, l) << "\n\n";

    // abs ou fabs = Arredonda o valor absoluto de numerais
    double m = -15, n = -9;
    cout << fabs(m) << endl;
    cout << fabs(n) << endl;

    return 0;
}