#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    fstream arquivo;
    string linha;
    char linha_b[255];

    arquivo.open("cfbcursos.txt", fstream::in | fstream::out | fstream::app);

    // in = input(leitura)
    // out = output(escrita)
    // binary = modo binário
    // ate = abre para escrita e posiciona no final
    // app = append, abre para escrita sem deletar o conteúdo atual, posiciona no final
    // trunc = truncate, abre para escrita e remove o conteúdo atual antes de abrir

    if (arquivo.is_open())
    {
        arquivo << "Curso de C++" << endl;
        arquivo << "Biblioteca fstream" << endl;
    }
    else
    {
        cout << "Arquivo nao esta aberto" << endl;
    }

    arquivo.close();
    cout << endl;

    ///////////////////////////////////////////////////////////////////////

    arquivo.open("cfbcursos.txt", fstream::in);
    if (arquivo.is_open())
    {
        while (getline(arquivo, linha))
            cout << linha << endl;
    }
    else
    {
        cout << "Arquivo nao esta aberto" << endl;
    }
    arquivo.close();
    cout << endl;

    // write -> Escreve no arquivo

    arquivo.open("cfbcursos.txt", fstream::in | fstream::app);
    if (arquivo.is_open())
    {
        arquivo.write("\nwww.youtube.com/cfbcursos\n", 26);
    }
    else
    {
        cout << "Arquivo nao esta aberto" << endl;
    }
    arquivo.close();
    cout << endl;

    arquivo.open("cfbcursos.txt", fstream::in);
    while (getline(arquivo, linha))
    {
        cout << linha << endl;
    }
    arquivo.close();
    cout << endl;

    // read -> Lê do arquivo
    arquivo.open("cfbcursos.txt", fstream::in);
    arquivo.read(linha_b, 255);
    cout << linha_b << endl;
    arquivo.close();
    cout << endl;

    // tellip = Retorna a posição do ponteiro dentro do stream
    // seekp = Define a posição do ponteiro dentro do stream

    long pos;
    arquivo.open("cfbcursos.txt", fstream::out);
    arquivo.write("CFB Aulas", 9);
    pos = arquivo.tellp(); // Posição 9
    cout << pos << endl;
    arquivo.seekp(pos - 5);
    pos = arquivo.tellp(); // Posição 4
    cout << pos << endl;
    arquivo.write("Cursos", 6);
    arquivo.close();
    cout << endl;

    // beg, cur, end = Constantes para definir a posição no stream
    long pos2;
    arquivo.open("cfbcursos.txt", fstream::out);
    arquivo.write("CFB Aulas", 9);
    pos2 = arquivo.tellp();
    cout << pos2 << endl;
    arquivo.seekp(arquivo.beg + 4);
    pos2 = arquivo.tellp();
    cout << pos2 << endl;
    arquivo.write("Cursos", 6);
    arquivo.close();
    cout << endl;

    return 0;
}