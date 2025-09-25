#include <iostream>
#include <ctime> // time.h
#include <cmath> //math.h

using namespace std;

int main()
{
    size_t tam;
    clock_t c;
    time_t t;
    struct tm *infoTempo;

    char buffer[80];
    char buffer2[80];
    char buffer3[80];
    char buffer4[80];

    time(&t);
    infoTempo = localtime(&t);

    strftime(buffer, 80, "Hora: %I:%M:%S", infoTempo);
    strftime(buffer2, 80, "Data: %d/%m/%Y", infoTempo);

    cout << buffer << endl;
    cout << buffer2 << endl;

    return 0;
}

/*
    int numeros_primos(int n)
{
    int i, j;
    int freq = n - 1;
    for (i = 2; i <= n; ++i)
    {
        for (j = sqrt(i); j > 1; --j)
        {
            if (i % j == 0)
            {
                --freq;
                break;
            }
        }
    }
    return freq;
}

    int primos;
    clock_t t;
    t = clock();
    primos = numeros_primos(999999);
    t = clock() - t;

    cout << "Qtde de primos: " << primos << endl;
    cout << "Tempo de CPU: " << ((float)t/CLOCKS_PER_SEC) << " segundos" << endl;
*/

/*
    int primos;
    clock_t t1, t2, t3;
    t1 = clock();
    primos = numeros_primos(90000);
    t2 = clock();
    t3 = difftime(t2,t1);

    cout << "Qtde de primos: " << primos << endl;
    cout << "Tempo de CPU: " << ((float)t3 / CLOCKS_PER_SEC) << " segundos" << endl;

*/

/*
    time_t t;
    struct tm *infoTempo;
    // tm_sec - segundo = 0-60
    // tm_min - minuto = 0-59
    // tm_hour - hora = 0-23
    // tm_mday - dia do mês = 1-31
    // tm_mon - Mês = 0-11
    // tm_year - Ano desde 1900
    // tm_wady - Dia da Semana = 0-6
    // tm_yday - Dia do Ano = 0-365
    // tm_isdst - Daylight Saving Time Flag

    time(&t);
    infoTempo = localtime(&t);

    cout << t << " segundos desde 00:00 de 1 de Janeiro de 1970" << endl;
    cout << asctime(infoTempo);
    cout << infoTempo->tm_sec << endl;
    cout << infoTempo->tm_min << endl;
    cout << infoTempo->tm_hour << endl;

*/

/*
    time_t t;
    // struct tm *infoTempo;

    time(&t);
    // infoTempo = localtime(&t);

    // cout << asctime(infoTempo) << endl;
    cout << ctime(&t) << endl;
*/