#include <iostream>

using namespace std;

int main()
{
    char nome[80];
    char n, s;

    n = cin.get();
    cin.ignore(80, ' ');
    s = cin.get();
    cout << n << " - " << s << endl;

    return 0;
}