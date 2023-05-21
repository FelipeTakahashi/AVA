#include <Servo.h> 

Servo servo;

int potenciometro = 0;

int valor = 0; 

void setup (){
	
  servo.attach(6); 
}

void loop(){

  valor = analogRead(potenciometro); 

  valor = map(valor, 0, 1024, 0, 180);
  servo.write(valor); 
  
  delay(10);  
}
