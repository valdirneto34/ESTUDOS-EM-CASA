#define ledR 2
#define ledG 4
#define ledB 3
#define botao 7

class Btn{
public:
  int btnclicado, btnliberado, pino;
  Btn(int p){
    pino=p;
    btnclicado=0;
    btnliberado=0;
  }
  bool press(){
    if(digitalRead(pino)==1){
      btnclicado=1;
      btnliberado=0;
    }else{
      btnliberado=1;
    }
    if((btnclicado==1) and (btnliberado==1)){
      btnclicado=0;
      btnliberado=0;
      return true;
    }else{
      return false;
    }
  }
};

class Cor{
public:
  int pinoR, pinoG, pinoB, ciclo, maximo;
  Cor(int pr, int pg, int pb):pinoR(pr),pinoG(pg),pinoB(pb){
    ciclo=0;
    maximo=8;
  }
  void trocaLed(){
    if(ciclo==0){
      corLed(1,0,0); //VERMELHO
    }else if(ciclo==1){
      corLed(0,1,0); //VERDE
    }else if(ciclo==2){
      corLed(0,0,1); //AZUL
    }else if(ciclo==3){
      corLed(1,1,1); //BRANCO
    }else if(ciclo==4){
      corLed(1,0,1); //MAGENTA
    }else if(ciclo==5){
      corLed(1,1,0); //AMARELO
    }else if(ciclo==6){
      corLed(0,1,1); //CIANO
    }else if(ciclo==7){
      corLed(0,0,0); //LED APAGADO
    }
    ciclo++;
    if(ciclo>maximo-1){
      ciclo=0;
    }
  }
private:
  void corLed(int r, int g, int b){
    digitalWrite(pinoR,r);
    digitalWrite(pinoG,g);
    digitalWrite(pinoB,b);
  }
};

Btn btn(botao);
Cor cor(ledR, ledG, ledB);

void setup() {
  pinMode(ledR, OUTPUT);
  pinMode(ledG, OUTPUT);
  pinMode(ledB, OUTPUT);
  pinMode(botao, INPUT);
}

void loop() {
  if(btn.press()){
    cor.trocaLed();
  }
}
