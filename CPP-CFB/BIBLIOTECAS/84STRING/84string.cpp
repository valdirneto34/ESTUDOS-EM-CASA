#include <iostream>
#include <string>

using namespace std;

int main()
{
    string txt("CFB Cursos - Curso de C++ - Serie sobre bibliotecas - www.youtube.com/cfbcursos");

    cout << txt << endl;
    cout << txt.capacity() << endl;
    txt.resize(10);
    txt.shrink_to_fit();
    cout << txt << endl;
    cout << txt.capacity() << endl;


    return 0;
}

/*
    string txt("CFB Cursos - Curso de C++");
    string::iterator it;

    it=txt.begin();


    //rbegin
    //rend
    //reverse_iterator

*/

/*
    string txt("CFB Cursos - Curso de C++");

    cout << txt << endl;
    cout << txt.size() << endl;
    txt.resize(10);
    cout << txt.size() << endl;
    cout << txt << endl;
    cout << txt.capacity() << endl;
*/

/*
    string txt("CFB Cursos - Curso de C++");

    txt.clear();

    if(txt.empty()){
        cout << "String vazia" << endl;
    }else{
        cout << txt << endl;
    }
*/