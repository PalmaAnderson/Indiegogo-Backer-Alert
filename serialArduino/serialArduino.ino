
const int PIN = 8;
int incomingByte = 0;
void setup() {
  Serial.begin(9600);    //configura comunicação serial com 9600 bps
  pinMode(PIN,OUTPUT);   //configura pino do led como saída
}

void loop() {

        // send data only when you receive data:
        if (Serial.available() > 0) {
          
                incomingByte = Serial.read();

                
                if (incomingByte=='A') {
                  
                    digitalWrite(PIN,HIGH); 
                    delay(1000);
                    digitalWrite(PIN,LOW);
                }
                
        
    }
  }


