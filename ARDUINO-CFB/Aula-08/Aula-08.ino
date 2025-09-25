#define ledR 2
#define ledG 4
#define ledB 3
#define botao 7
#define maximo 8

int btnclicado = 0;
int btnliberado = 0;
int ciclo = 0;

void vermelho(){
  digitalWrite(ledR, 1);
  digitalWrite(ledG, 0);
  digitalWrite(ledB, 0);
}
void verde(){
  digitalWrite(ledR, 0);
  digitalWrite(ledG, 1);
  digitalWrite(ledB, 0);
}
void azul(){
  digitalWrite(ledR, 0);
  digitalWrite(ledG, 0);
  digitalWrite(ledB, 1);
}
void branco(){
  digitalWrite(ledR, 1);
  digitalWrite(ledG, 1);
  digitalWrite(ledB, 1);
}
void amarelo(){
  digitalWrite(ledR,1);
  digitalWrite(ledB,0);
  digitalWrite(ledG,1);
}
void magenta(){
  digitalWrite(ledR,1);
  digitalWrite(ledB,1);
  digitalWrite(ledG,0);
}
void ciano(){
  digitalWrite(ledR,0);
  digitalWrite(ledB,1);
  digitalWrite(ledG,1);
}
void apagado(){
  digitalWrite(ledR,0);
  digitalWrite(ledB,0);
  digitalWrite(ledG,0);
}

void trocaLed(){
  if(ciclo == 0){
    vermelho();
  }else if(ciclo == 1){
    verde();
  }else if(ciclo == 2){
    azul();
  }else if(ciclo == 3){
    amarelo();
  }else if(ciclo == 4){
    branco();
  }else if(ciclo == 5){
    magenta();
  }else if(ciclo == 6){
    ciano();
  }else if(ciclo == 7){
    apagado();
  }
  ciclo++;
  if (ciclo>maximo-1){
    ciclo = 0;
  }
}

void verificaBtn(){
  if(digitalRead(botao)==HIGH){
    btnclicado = 1;
    btnliberado = 0;
  }else{
    btnliberado = 1;
  }
  if(btnclicado==1 and btnliberado == 1){
    btnliberado = 0;
    btnclicado = 0;
    trocaLed();
  }
}

void setup() {
  pinMode(ledR, OUTPUT);
  pinMode(ledG, OUTPUT);
  pinMode(ledB, OUTPUT);
  pinMode(botao, INPUT);
}

void loop() {
  verificaBtn();
}
