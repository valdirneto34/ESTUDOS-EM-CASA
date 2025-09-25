#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<string> produtos = {"Mouse", "Teclado", "Monitor", "Gabinete", "Cx.Som"};
    vector<string>::iterator it;
    cout << "----IMPRESSAO SEM FOR----\n";
    it = produtos.begin();        // Início do vector
    cout << *it << endl;          // Imprimi o índice 0
    advance(it, 1);               // Avança 1 no vector
    cout << *it << endl;          // Imprimi o índice 1
    it = produtos.begin();        // Início do vector
    cout << *next(it, 2) << endl; // Imprimi o índice 2
    it = produtos.end();          // Final do vector
    cout << *prev(it, 2) << endl; // Imprimi o índice 3
    it = produtos.end() - 1;      // END Retorna a qtd de elementos(necessita de -1 para ver o último)
    cout << *it << endl;          // Imprimi o índice 4(último)
    cout << "-------------------------\n\n";
    cout << "----IMPRESSAO COM FOR----" << endl;
    for (it = produtos.begin(); it != produtos.end(); it++)
    {
        cout << *it << endl;
    }
    cout << "-------------------------\n";
    /*
    // PODE SER USADO ESSE SE O ITERATOR TIVER APENAS ESSA FUNÇÃO
    for (vector<string>::iterator it = produtos.begin(); it != produtos.end(); it++)
    {
        cout << *it << endl;
    }
    */

    return 0;
}