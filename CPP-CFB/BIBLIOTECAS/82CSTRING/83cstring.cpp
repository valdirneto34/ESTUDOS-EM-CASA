#include <iostream>
#include <cstring> //string.h

using namespace std;

int main()
{
    char txt[] = "CFB Cursos, Curso de C++ - www.youtube.com/cfbcursos";
    int tam;

    tam = strlen(txt);

    cout << tam << endl;

    return 0;
}

/*
    char *txt1;
    char txt2[] = "CFB Cursos";
    char pesquisa = 'B';

    txt1 = (char *)memchr(txt2, pesquisa, strlen(txt2));
    if (txt1 != NULL)
    {
        cout << "Letra " << pesquisa << " encontrada na posicao: ";
        cout << txt1 - txt2 + 1 << endl;
    }
    else
    {
        cout << "Letra " << pesquisa << " nao encontrada";
    }
*/

/*
    char txt[] = "CFB Cursos";
    char *c;
    char pesquisa='C';

    c= strchr(txt,pesquisa);

    cout << "Posicao: " << c-txt+1;
*/

/*
    char txt[]="CFB Cursos - Curso de C++ - www.youtube.com/cfbcursos";
    char chave[]="ytw";
    int i;

    i=strcspn(txt,chave);

    cout << "Pos: " << i << " - " << txt[i] << endl;
*/

/*
    char txt[] = "CFB Cursos - Curso de C++ - www.youtube.com/cfbcursos";
    char *c;
    char pesquisa = 'o';

    c = strrchr(txt, pesquisa);

    cout << "Pos: " << c-txt << endl;

*/

/*
    char txt[] = "CFB Cursos, Curso de C++ - www.youtube.com/cfbcursos";
    char *c;

    c = strtok(txt,",-");
    while(c!=NULL){
        cout << c << endl;
        c = strtok(NULL,",-");

    }
*/