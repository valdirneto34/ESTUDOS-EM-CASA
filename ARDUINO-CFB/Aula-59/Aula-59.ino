#include <Keypad.h>

#define linhas 4
#define colunas 4
char mapaTeclas[4][4] = {
  { '1', '2', '3', 'A' },
  { '4', '5', '6', 'B' },
  { '7', '8', '9', 'C' },
  { '*', '0', '#', 'D' }
};

byte pinos_linha[linhas] = { 6, 7, 8, 9 };
byte pinos_coluna[colunas] = { 10, 11, 12, 13 };

Keypad teclado = Keypad(makeKeymap(mapaTeclas), pinos_linha, pinos_coluna, linhas, colunas);

void setup() {
  Serial.begin(9600);
}

void loop() {
  char tecla = teclado.getKey();
  if(tecla!= NO_KEY){
    Serial.println(tecla);
  }
}
