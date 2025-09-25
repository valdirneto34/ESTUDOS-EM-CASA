#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> vct = {0, 1, 2, 3, 4};
    vector<int> vct2 = {5, 6, 7, 8, 9};

    vct.emplace_back(9);

    for (auto x : vct)
    {
        cout << x << endl;
    }

    return 0;
}

/*
    vector<int> vct = {9, 2, 7, 4, 5, 6, 3, 8, 0, 1, 3, 2, 5};
    vector<int> vct2;

    for (auto it = vct.begin(); it != vct.end(); it++)
    {
        cout << *it << endl;
    }
    // REVRSE ITERATOR
    for (auto it = vct.rbegin(); it != vct.rend(); it++)
    {
        cout << *it << endl;
    }
    cout << vct.size() << endl; // TAMANHO ATUAL
    cout << vct.max_size() << endl; // TAMANHO MÁXIMO
    vct.resize(5); // REDMENSIONA O VECTOR
    cout << vct.capacity() << endl; // TAMANHO MÁXIMO QUE O VECTOR JÁ TEVE
    vct.shrink_to_fit(); // MUDA O CAPACITY PARA O Nº DE ELEMENTOS ATUAL
    cout << vct[3] << endl;
    cout << vct.at(3) << endl;
    cout << vct.front() << endl;
    cout << vct.back() << endl;
    vct = {9, 2, 7, 4, 5, 6, 3, 8, 0, 1};
    vct2.assign(10,0);
    for (auto x:vct2)
    {
        cout << x << endl;
    }
    vct.push_back(0);
    vct.pop_back();
    vector<int>::iterator it;
    it = vct.begin();
    vct.insert(it, 5);
    it = vct.end();
    vct.insert(it, 5, 9);
    it = vct.end() - 1;
    vct.erase(it);
    vct.erase(vct.begin()+6,vct.end());
    vector<int> vct = {0, 1, 2, 3, 4};
    vector<int> vct2 = {5, 6, 7, 8, 9};
    vct.swap(vct2);
    vct2.clear();
    // ADICIONA 9 NA POS 2, SEM REMOVER O Nº QUE JÁ OCUPA A POSIÇÃO
    vct.emplace(vct.begin() + 2, 9);
    vct.emplace_back(9); // INSERE NO FINAL
*/