#include <iostream>
#include <vector>

using namespace std;

int main()
{

    int x1, x2, x3, x4;
    x1 = 10;
    x2 = 5;
    x3 = 2;
    x4 = 12;
    auto soma = [=]() -> int
    {
        return x1 + x2 + x3 + x4;
    };
    auto maior = [=](vector<int> n) -> int
    {
        auto m = 0;
        for (auto x : n)
        {
            m = (m > x) ? m : x;
        }
        return m + x1 + x2 + x3 + x4;
    };
    cout << maior({9, 8, 2, 10, 45, 20, 5, 34, 12, 7, 100}) << endl;
    cout << soma() << endl;
    cout << maior({1, 2, 3, 4, 5, 6, 7, 8, 9, 0}) << endl;
    return 0;
}