#include <Keypad.h>

#define linhas 4
#define colunas 4
#define led_vermelho 2
#define led_amarelo 3
#define led_verde 4
char mapaTeclas[4][4] = {
  { '1', '2', '3', 'A' },
  { '4', '5', '6', 'B' },
  { '7', '8', '9', 'C' },
  { '*', '0', '#', 'D' }
};
String senha = "123";
String digitada;
int estado = 0;
byte pinos_linha[linhas] = { 6, 7, 8, 9 };
byte pinos_coluna[colunas] = { 10, 11, 12, 13 };

Keypad teclado = Keypad(makeKeymap(mapaTeclas), pinos_linha, pinos_coluna, linhas, colunas);

void setup() {
  pinMode(led_vermelho, OUTPUT);
  pinMode(led_verde, OUTPUT);
  pinMode(led_amarelo, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  char tecla = teclado.getKey();
  if (tecla != NO_KEY) {
    estado = 1;
    if (tecla == '#') {
      if (verificaSenha(senha, digitada)) {
        estado = 3;
        leds(estado);
        delay(3000);
        estado = 0;
      } else {
        estado = 2;
        leds(estado);
        delay(3000);
        estado = 0;
      }
      digitada = "";
    } else {
      digitada += tecla;
    }
    leds(estado);
  }
}

bool verificaSenha(String sa, String sd) {
  bool res = false;
  if (sa.compareTo(sd) == 0) {
    res = true;
  } else {
    res = false;
  }
  return res;
}

void leds(int estado) {
  //0=Aguardando / 1=Digitando / 2=Negado / 3=Aceito
  if (estado == 0) {
    digitalWrite(led_vermelho, 0);
    digitalWrite(led_verde, 0);
    digitalWrite(led_amarelo, 0);
  } else if (estado == 1) {
    digitalWrite(led_vermelho, 0);
    digitalWrite(led_verde, 0);
    digitalWrite(led_amarelo, 1);
  } else if (estado == 2) {
    digitalWrite(led_vermelho, 1);
    digitalWrite(led_verde, 0);
    digitalWrite(led_amarelo, 0);
  } else if (estado == 3) {
    digitalWrite(led_vermelho, 0);
    digitalWrite(led_verde, 1);
    digitalWrite(led_amarelo, 0);
  }
}