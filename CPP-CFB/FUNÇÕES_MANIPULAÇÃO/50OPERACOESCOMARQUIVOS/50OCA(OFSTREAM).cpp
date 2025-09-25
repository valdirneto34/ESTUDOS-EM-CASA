#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    // oftream, ifstream, fstream

    ofstream arquivo;

    arquivo.open("cfbcursos.txt", ios::app);

    arquivo << "CFB Cursos\n";
    arquivo << "Curso de C++\n";
    arquivo << "cfbcursos.com.br\n";
    arquivo << "youtube.com/cfbcursos\n";

    arquivo.close();

    return 0;
}