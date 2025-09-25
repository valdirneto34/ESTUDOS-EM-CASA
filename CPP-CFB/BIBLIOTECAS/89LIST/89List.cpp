#include <iostream>
#include <list>

using namespace std;

bool par(const int &value)
{
    return ((value % 2) == 0);
}

int main()
{
    list<int> lst1 = {0, 1, 2, 3, 4};
    list<int> lst2 = {5, 6, 7, 8, 9};

    lst1.merge(lst2);
    lst1.reverse();

    for (auto x : lst1)
        cout << x << "  ";
    cout << endl;

    return 0;
}

/*
    list<int> lst1;
    list<int> lst2(10, 0);
    list<int> lst3(lst2);
    list<int> lst4 = {1, 2, 3, 4};

    for (auto it = lst4.begin(); it != lst4.end(); it++)
        cout << *it << "  ";
    cout << endl;
    cout << "Tamanho: " << lst4.size() << endl;
    cout << "Capacidade maxima: " << lst4.max_size() << endl;
    cout << "Primeiro elemento: " << lst4.front() << endl;
    cout << "Ultimo elemento: " << lst4.back() << endl;

    if (lst4.empty())
        cout << "Lista vazia" << endl;
    else
        cout << "Lista nao esta vazia" << endl;
*/
/*
    lst2.assign(lst1.begin(),lst1.end());
    lst1.push_back(8);
    lst1.push_front(9);
    lst1.pop_back();
    lst1.pop_front();
    list<int>::iterator it;
    it=lst1.begin();
    ++it;
    lst1.insert(it, 8);
    lst1.erase(it);
*/
/*
    list<int> lst1 = {1, 2, 3, 4, 5};
    list<int> lst2 = {6, 7, 8, 9, 10};
    lst1.swap(lst2);
    lst1.clear();
    lst2.resize(3);
    for (auto x : lst1)
        cout << x << "  ";
    cout << endl;
    for (auto x : lst2)
        cout << x << "  ";
    cout << endl;
    lst1.emplace(++ ++ ++lst1.begin(), 9);
    lst1.emplace_back(9);
    lst1.emplace_front(9);
    lst1.remove(0); // REMOVE TODOS OS ZEROS
*/
/*
    bool par(const int &value)
    {
        return ((value % 2) == 0);
    }
    bool impar(const int &value)
    {
        return ((value % 2) == 1);
    }
    list<int> lst1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};

    lst1.remove_if(par);

    for (auto x : lst1)
        cout << x << "  ";
    cout << endl;
    lst1.sort(); // ORDENA A LISTA
    lst1.unique(); // DEIXA APENAS UM VALOR DE CADA
    lst1.merge(lst2); // MESCLA AS DUAS LISTAS
    lst1.reverse(); // ORDENA AO CONTRÁRIO DO SORT
*/