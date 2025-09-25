#include <iostream>
#include <cctype> //ctype.h

using namespace std;

int main()
{
    char str[] = "cfb-cursos";
    char c;
    int i = 0;

    while (str[i])
    {
        c = str[i];
        putchar(toupper(c));
        // tolower
        i++;
    }
    return 0;
}

/*
    isalnum
    isalpha
    isspace
    iscntrl \n
    isdigit
    islower
    isprint \n
    ispunct,.?!
    isupper
    isxdigit
*/

/*
    if(isalpha(str[i])){
            cout << "Caractere " << str[i] << " e alfabetico" << endl;
        }
        else{
            cout << "Caractere " << str[i] << " NAO e alfabetico" << endl;

        }
*/

/*
    char str[] = ">> CFB-Cursos <<";
    int i = 0,cont=0;

    while (str[i])
    {
        if(isspace(str[i])){
            cont++;
        }
        i++;
    }
    cout << cont << endl;
*/