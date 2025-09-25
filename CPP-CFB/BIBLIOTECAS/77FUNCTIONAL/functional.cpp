#include <iostream>
#include <functional>

using namespace std;

struct cfb
{
    int num;
    int dobro()
    {
        return num * 2;
    }
};

class Cfb
{
public:
    int num;
    Cfb(int n) : num(n) {};
    int dobro()
    {
        return num * 2;
    }
};

int main()
{
    cfb n1{10};
    cfb n2{5};
    Cfb n3{10};
    Cfb n4{5};

    auto dobro2 = mem_fn(&cfb::dobro);
    auto dobro3 = mem_fn(&Cfb::dobro);

    cout << dobro2(n1) << endl;
    cout << dobro2(n2) << "\n\n";
    cout << dobro3(n3) << endl;
    cout << dobro3(n4) << endl;

    return 0;
}

/*
    int soma(int n1, int n2)
    {
        return n1 + n2;
    }
    int n1 = 10;
    const int n2 = 5;
    auto s1 = bind(soma, n1, n2);
    cout << s1() << endl;
*/

/*
    int n1 = 10;
    auto n2 = cref(n1);
    n1++;
    cout << n2 << endl;
*/