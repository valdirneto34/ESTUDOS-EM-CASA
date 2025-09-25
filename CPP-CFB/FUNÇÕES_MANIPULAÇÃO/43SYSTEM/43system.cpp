#include <iostream>
#include <stdlib.h>
#include <unistd.h>

using namespace std;

int main()
{
    system("dir");
    system("cls");
    // system("color/?");
    system("dir");
    system("color 47");
    sleep(2);
    system("color 46");
    sleep(2);
    system("color 06");
    sleep(2);
    system("pause");
    
    system("color 06");
    cout << "Canal Fessor Bruno" << endl;
    sleep(5);
    system("color 07");
    cout << "Canal Fessor Bruno" << endl;
    sleep(5);
    system("color 08");
    cout << "Canal Fessor Bruno" << endl;

    system("pause");
    return 0;
}