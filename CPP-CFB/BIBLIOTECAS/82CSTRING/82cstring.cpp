#include <iostream>
#include <cstring> //string.h

using namespace std;

int main()
{
    int res;

    char txt1[80] = "Curso de programacao";
    char txt2[80] = "CFB Cursos";

    res = strcmp(txt1,txt2);
    //res = strncmp(txt1,txt2,5); // COMPARA ATÉ O NÚMERO APENAS
    //memcmp(txt1,txt2,sizeof(txt1)); // COMPARA BLOCOS DE MEMÓRIA

    if(res==-0){
        cout << "Iguais" << endl;
    }else{
        cout << "Diferentes" << endl;
    }

    /*
        0 = iguais
        >0 = 1 maior que 2
        <0 = 2 maior que a 1
    */

    return 0;
}

/*
    char txt1[50]="Curso de programacao";
    char txt2[50]="";
    char txt3[50]="";

    strcpy(txt2,txt1);
    strncpy(txt3,txt1,5);
    memcpy(txt2,txt1,sizeof(txt1)+1);

    cout << txt2 << endl;
    cout << txt3 << endl;
*/

/*
    struct{
        char nome[40];
    }pessoa1,pessoa2;

    char meunome[50]="Valdir";

    memcpy(pessoa1.nome,meunome,strlen(meunome)+1);
    memcpy(pessoa2.nome,pessoa1.nome,strlen(meunome)+1);

    cout << pessoa1.nome << endl;
    cout << pessoa2.nome << endl;
*/

/*
    char txt[80] = "Curso de programacao";
    char txt2[80] = " - CFB Cursos";

    strcat(txt, txt2);
    //strncat(txt, txt2,6); // ESCOLHE QUANTOS CARACTERES

    cout << txt << endl;
*/