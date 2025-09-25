#include <iostream>
#include <string>

using namespace std;

int main()
{
    string txt1("18"), txt2;
    int ano = 2018, res;

    res = ano - stoi(txt1);
    txt2 = to_string(res);

    cout << res << endl;
    cout << txt2 << endl;

    /*
        stol
        stoll
        stoul
        stoull
        stof
        stod
        stold
    */

    return 0;
}

/*
    string txt1("Curso de C++ - Biblioteca string");
    string txt2;

    size_t encontrado=txt1.find("ring");

    if(encontrado!=string::npos){
        cout << "Encontrado na posicao " << encontrado << endl;
    }else{
        cout << "NAO encontrado" << endl;
    }
*/

/*
    string txt1("Curso de C++ - Biblioteca string");
    string txt2;

    txt2 = txt1.substr(15,10);

    cout << txt2 << endl;
*/

/*
    string txt1("Curso de C++");
    string txt2("CFB Cursos");

    if(txt1.compare(txt2)==0){
        cout << "Strings iguais" << endl;
    }else{
        cout << "Strings diferentes" << endl;
    }
*/