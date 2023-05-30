int potenciometro = 0;

int valor = 0; 

void setup (){ 
  Serial.begin(9600);
}

void loop(){

  valor = analogRead(potenciometro); 

  valor = map(valor, 0, 1024, 500, 1500);
  tone(11, valor, 10); 
  Serial.println(valor);
  
  delay(10);  
}
