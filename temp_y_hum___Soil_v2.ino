// Incluimos librería
#include <DHT.h>
 
// Definimos el pin digital donde se conecta el sensor
#define DHTPIN 2
// Dependiendo del tipo de sensor
#define DHTTYPE DHT11
 
// Inicializamos el sensor DHT11
DHT dht(DHTPIN, DHTTYPE);
int moisture = 0;

void setup() {
  // Inicializamos comunicación serie
  Serial.begin(9600);
   // Comenzamos el sensor DHT
  dht.begin();
  
  pinMode(A0, OUTPUT); //soil
  pinMode(A1, INPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
}
  
void loop() {
    // Esperamos 5 segundos entre medidas
  delay(5000);

//soil
    // Aplique energía al sensor de humedad del suelo
    digitalWrite(A0, HIGH);
    delay(10); // Esperar por 10 millisecond(s)
    moisture = analogRead(A1);
    // Apague el sensor para reducir la corrosión del metal.
    // over time
    digitalWrite(A0, LOW);
    Serial.print("Moisture Sensor Value:"); 
    Serial.println(moisture);
    digitalWrite(8, LOW);
    digitalWrite(9, LOW);
    digitalWrite(10, LOW);
    digitalWrite(11, LOW);
    digitalWrite(12, LOW);
    
 
  // Leemos la humedad relativa
  float h = dht.readHumidity();
  // Leemos la temperatura en grados centígrados (por defecto)
  float t = dht.readTemperature();
 
  // Comprobamos si ha habido algún error en la lectura
  if (isnan(h) || isnan(t)) {
    Serial.println("Error obteniendo los datos del sensor DHT11");
    return;
  }

 if (moisture < 200) {
      digitalWrite(8, HIGH);
    } else {
      if (moisture < 400) {
        digitalWrite(9, HIGH);
      } else {
        if (moisture < 600) {
          digitalWrite(10, HIGH);
        } else {
          if (moisture < 800) {
            digitalWrite(11, HIGH);
          } else {
            digitalWrite(12, HIGH);
          }
        }
      }
    } 
    
  Serial.print("Humedad aire: ");
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("Temperatura aire: ");
  Serial.print(t);
  Serial.print(" *C\n ");
}
