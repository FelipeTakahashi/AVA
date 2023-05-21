const int ledRed = 12;
const int ledGreen = 11;
const int ledBlue = 10;
const int ledYellow = 9;
const int pot = 0;
int variacao = 0;

void setup() {
  pinMode(ledRed, OUTPUT);
  pinMode(ledGreen, OUTPUT);
  pinMode(ledBlue, OUTPUT);
  pinMode(ledYellow, OUTPUT);
}

void loop() {
  variacao = analogRead(pot);
  
  digitalWrite(ledRed, HIGH);
  delay(variacao);
  digitalWrite(ledRed, LOW);
  delay(variacao);
  
  digitalWrite(ledGreen, HIGH);
  delay(variacao/2);
  digitalWrite(ledGreen, LOW);
  delay(variacao/2);
  
  digitalWrite(ledBlue, HIGH);
  delay(variacao/3);
  digitalWrite(ledBlue, LOW);
  delay(variacao/3);
  
  digitalWrite(ledYellow, HIGH);
  delay(variacao/4);
  digitalWrite(ledYellow, LOW);
  delay(variacao/4);
}
