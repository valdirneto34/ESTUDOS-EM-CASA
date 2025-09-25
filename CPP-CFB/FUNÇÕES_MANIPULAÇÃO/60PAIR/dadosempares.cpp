#include <iostream>
#include <utility>
#include <vector>

using namespace std;

int main()
{
    const int tam = 3;

    vector<pair<int, string>> prod;

    pair<int, pair<string, double>> par[tam];

    par[0] = make_pair(10, make_pair("Mouse", 10.55));
    par[1] = make_pair(20, make_pair("Teclado", 50.49));
    par[2] = make_pair(30, make_pair("Monitor", 399.98));

    prod.push_back(make_pair(10, "Mouse"));
    prod.push_back(make_pair(20, "Teclado"));
    prod.push_back(make_pair(30, "Monitor"));

    for (int i = 0; i < tam; i++)
    {
        cout << par[i].first << " - " << par[i].second.first;
        cout << " - " << par[i].second.second << endl;
    }
    cout << endl;
    for (auto i : prod)
    {
        cout << i.first << " - " << i.second << endl;
    }

    return 0;
}