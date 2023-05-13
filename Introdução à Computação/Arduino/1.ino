const int ledRed = 13;
const int ledYellow = 12;
const int ledGreen = 11;
const int ledRedP = 7;
const int ledGreenP = 6;

int t1 = 4000;
int t2 = t1/2;
int t3 = 500;

void setup() {
  pinMode(ledRed, OUTPUT);
  pinMode(ledYellow, OUTPUT);
  pinMode(ledGreen, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  // Vermelho pra carro
  digitalWrite(ledGreenP, HIGH);
  digitalWrite(ledRed, HIGH);
  	delay(t1);
  
  digitalWrite(ledGreenP, LOW);
  digitalWrite(ledRed, LOW); 
  	delay(t3);
  
  // Amarelo
  digitalWrite(ledYellow, HIGH); 
  	delay(t2); 
  digitalWrite(ledYellow, LOW); 
  	delay(t3);
  
  // Verde pra carro
  digitalWrite(ledRedP, HIGH);
  digitalWrite(ledGreen, HIGH); 
  	delay(t1);
  
  digitalWrite(ledRedP, LOW);
  digitalWrite(ledGreen, LOW);    
  	delay(t3);
}
