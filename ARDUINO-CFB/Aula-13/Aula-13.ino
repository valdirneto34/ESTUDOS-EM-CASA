#define ldr A0
#define led 2
int vldr = 0;

void setup() {
  pinMode(ldr, INPUT);
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  vldr = analogRead(ldr);
  if (vldr < 700) {
    digitalWrite(led, 0);
  } else {
    digitalWrite(led, 1);
  }
  Serial.println(vldr);
  delay(100);
}
