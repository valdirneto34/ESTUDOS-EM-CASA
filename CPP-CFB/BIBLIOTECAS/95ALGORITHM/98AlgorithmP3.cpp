#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    // replace_if = Substitui valores da coleção que atendam a determinada consição
    cout << "replace_if" << endl;
    vector<int> vt1{1, 4, 7, 2, 5, 8, 3, 6, 9, 0};
    replace_if(vt1.begin(), vt1.end(), [](int i)
               { return i < 5; }, 10);
    for (auto x : vt1)
        cout << x << "  ";
    cout << "\n\n";

    // fill = Preenche uma coleção com um valor especificado
    cout << "fill" << endl;
    vector<int> vt2(10);
    fill(vt2.begin(), vt2.end(), 10);
    for (auto x : vt2)
        cout << x << "  ";
    cout << "\n\n";

    // remove = Remove um valor indicado da coleção
    cout << "remove" << endl;
    vector<int> vt3{2, 1, 2, 3, 2, 4, 2, 5, 2, 6, 2, 7, 2, 8, 2, 9, 2};
    int qtde = count(vt3.begin(), vt3.end(), 2);
    remove(vt3.begin(),vt3.end(),2);
    vt3.resize(vt3.size() - qtde);
    vt3.shrink_to_fit();
    for (auto x : vt3)
        cout << x << "  ";
    cout << "\n\n";

    // unique = Remove elementos dupliacdos consecutivos na coleção
    cout << "unique" << endl;
    vector<int> vt4{0, 1, 2, 3, 3, 3, 4, 5, 2, 6, 7, 8, 9};
    vector<int>::iterator it;
    it = unique(vt4.begin(), vt4.end());
    vt4.resize(distance(vt4.begin(), it));
    for (auto x : vt4)
        cout << x << "  ";
    cout << "\n\n";

    // reverse = Inverte a ordem dos elementos
    cout << "reverse" << endl;
    vector<int> vt5{0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    reverse(vt5.begin(), vt5.end());
    for (auto x : vt5)
        cout << x << "  ";
    cout << "\n\n";

    // sort = Ordena os elementos da coleção
    cout << "sort" << endl;
    vector<int> vt6{9, 0, 8, 1, 7, 2, 6, 3, 5, 4};
    sort(vt6.begin(), vt6.end());
    for (auto x : vt6)
        cout << x << "  ";
    cout << "\n\n";

    // is_sorted = Verifica se a coleção está ordenada
    cout << "is_sorted" << endl;
    vector<int> vt7{9, 0, 8, 1, 7, 2, 6, 3, 5, 4};
    //sort(vt7.begin(), vt7.end());
    if (is_sorted(vt7.begin(), vt7.end()))
        cout << "Ordenada" << endl;
    else
        cout << "Colecao NAO ordenada" << endl;
    cout << "\n\n";

    // merge = Mescla duas coleções e armazena em um terceiro container
    cout << "merge" << endl;
    vector<int> vt8{0, 1, 2, 3, 4};
    vector<int> vt9{5, 6, 7, 8, 9};
    vector<int> vt10(10);
    merge(vt8.begin(), vt8.end(), vt9.begin(), vt9.end(), vt10.begin());
    for (auto x : vt10)
        cout << x << "  ";
    cout << "\n\n";

    // set_union = União de duas coleções
    cout << "set_union" << endl;
    vector<int> vt11{4, 0, 3, 2, 1};
    vector<int> vt12{9, 5, 8, 7, 6};
    vector<int> vt13(10);
    set_union(vt11.begin(), vt11.end(), vt12.begin(), vt12.end(), vt13.begin());
    for (auto x : vt13)
        cout << x << "  ";
    cout << "\n\n";

    // set_intersection = Interseção de duas coleções
    cout << "set_intersection" << endl;
    vector<int> vt14{0, 1, 2, 3, 4};
    vector<int> vt15{2, 3, 4, 5, 6};
    vector<int> vt16(3);
    set_intersection(vt14.begin(), vt14.end(), vt15.begin(), vt15.end(), vt16.begin());
    for (auto x : vt16)
        cout << x << "  ";
    cout << "\n\n";

    // set_diference = Retorna a diferença da primeira coleção em relação à segunda
    cout << "set_diference" << endl;
    vector<int> vt17{0, 1, 2, 3, 4};
    vector<int> vt18{2, 3, 4, 5, 6};
    vector<int> vt19(3);
    set_union(vt17.begin(), vt17.end(), vt18.begin(), vt18.end(), vt19.begin());
    for (auto x : vt19)
        cout << x << "  ";
    cout << "\n\n";

    // min e max = Retorna os menor e maior valores
    cout << "min e max" << endl;
    int n1 = 10, n2 = 5;
    cout << "Menor: " << min(n1, n2) << endl;
    cout << "Maior: " << max(n1, n2);
    cout << "\n\n";

    // minmax = Retorna os menor e maior valores dentre varios
    cout << "minmax" << endl;
    int n3 = 10, n4 = 5, n5 = 10, n6 = 3, n7 = 8, n8 = 9;
    auto res = minmax({n3, n4, n5, n6, n7, n8});
    cout << "Menor: " << res.first << " Maior: " << res.second;
    cout << "\n\n";

    // min_element, max_element, minmax_element
    cout << "min_element, max_element, minmax_element" << endl;
    vector<int> vt20{5, 4, 10, 30, 12, 15, 8, 7};
    vector<int>::iterator it1, it2;
    it1 = min_element(vt20.begin(), vt20.end());
    it2 = max_element(vt20.begin(), vt20.end());
    auto res2 = minmax_element(vt20.begin(), vt20.end());
    cout << "Menor: " << *it1 << " Maior: " << *it2 << endl;
    cout << "Menor: " << *res2.first << " Maior: " << *res2.second;
    cout << "\n\n";

    return 0;
}