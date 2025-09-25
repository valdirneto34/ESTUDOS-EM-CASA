#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;

int main()
{
    size_t tam;

    vector<int> num = {9, 6, 3, 8, 5, 2, 7, 4, 1, 0};

    tam = num.size();
    cout << tam << endl;

    return 0;
}

/*
    int num=-10;
    cout << abs(num) << endl;
*/

/*
    int num, den;
    div_t res;
    //ldiv_t PARA LONG INT
    //lldiv_t  PARA LONG LONG INT
    //size_t PRÓPRIO PARA TAMANHOS

    num = 10;
    den = 3;

    res = div(num, den);

    cout << num << " dividido por " << den << " = ";
    cout << res.quot << " resto " << res.rem << endl;

    // ldiv  MSM COISA QUE O DIV, PARA LONG INT
    // llabs LONG LONG ABS(ABSOLUTO) C++11
    // lldiv MSM COISA QUE O DIV, PARA LONG LONG C++11
*/