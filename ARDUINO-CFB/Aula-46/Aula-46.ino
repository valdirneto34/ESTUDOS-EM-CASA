#define btn 0  // INT 0 = Pino 2
int cont;

void reset() {
  cont = 100;
}

void setup() {
  attachInterrupt(btn, reset, RISING);
  // LOW
  // CHANGE
  //    RISING: LOW - HIGH
  //    FALLING: HIGH - LOW
  pinMode(btn, INPUT);
  Serial.begin(9600);
}

void loop() {
  for (cont = 100; cont > 0; cont--) {
    Serial.println(cont);
    delay(500);
  }
  Serial.println("Reiniciando Contagem!");
}