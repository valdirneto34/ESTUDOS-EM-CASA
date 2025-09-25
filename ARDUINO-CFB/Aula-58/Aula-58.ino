char mapaTeclas[4][4]={
                      {'1','2','3','A'},
                      {'4','5','6','B'},
                      {'7','8','9','C'},
                      {'*','0','#','D'}
};

void setup() {
  //pinos linhas - 6,7,8,9
  pinMode(6,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);

  //pinos colunas - 10,11,12,13
  pinMode(10,INPUT_PULLUP);
  pinMode(11,INPUT_PULLUP);
  pinMode(12,INPUT_PULLUP);
  pinMode(13,INPUT_PULLUP);

  Serial.begin(9600);
}

void loop() {
  for(int porta=6;porta<=9;porta++){
    digitalWrite(6,1);
    digitalWrite(7,1);
    digitalWrite(8,1);
    digitalWrite(9,1);
    digitalWrite(porta,0);

    if(digitalRead(10)==0){
      imp(porta-6,0);
      while(digitalRead(10)==0){}
    }
    if(digitalRead(11)==0){
      imp(porta-6,1);
      while(digitalRead(11)==0){}
    }
    if(digitalRead(12)==0){
      imp(porta-6,2);
      while(digitalRead(12)==0){}
    }
    if(digitalRead(13)==0){
      imp(porta-6,3);
      while(digitalRead(13)==0){}
    }

  }
}

void imp(int lin, int col){
  Serial.print(mapaTeclas[lin][col]);
  delay(100);
}
