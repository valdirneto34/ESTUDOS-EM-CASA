#include <iostream>
#include <string>

using namespace std;

int main()
{
    string txt("CFB Cursos - Curso de C++");
    string txt2 = "Javascript";

    // txt.append("Curso de C++"); // OU txt +=
    //  txt.push_back('B'); // APENAS 1 CARACTERE
    //  txt.pop_back();
    //  txt.assign("Curso de C++"); OU txt="Curso de C++";
    // txt.insert(10, " - ");
    // txt.erase(10,15);
    txt.replace(22, 4, txt2);
    cout << txt << endl;

    string txt3("Curso");
    string txt4("Aula");
    cout << txt3 << endl;
    cout << txt4 << endl;
    txt3.swap(txt4);
    cout << txt3 << endl;
    cout << txt4 << endl;

    return 0;
}

/*
    string txt("CFB Cursos - Curso de C++ - Serie sobre bibliotecas - www.youtube.com/cfbcursos");
    int tam = txt.size();

    cout << txt.at(2) << endl;
    cout << txt.back() << endl;
    txt.back() = 'B';
    cout << txt.back() << endl;

    cout << txt.front() << endl;

*/