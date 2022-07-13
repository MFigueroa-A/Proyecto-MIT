
#include <ESP8266WiFi.h> // Placa 8266
#include "DHT.h"        // Biblioteca de sensor de temperatura y humedad DHT11
#include <NTPClient.h>   //Conectarse a un servidor de tiempo 
#include <WiFiUdp.h> //WiFi UDP que puede enviar y recibir mensajes UDP
#include <time.h>   
#include "RTClib.h"  //Sensor RTC
RTC_DS3231 rtc;

#define DHTTYPE DHT11   // DHT 11
#define dht_dpin 0
#define D4 2            //Leds
#define D5 14
#define D6 12
#define D7 13
#define D8 15

const char* ssid     = "";      // SSID red wifi
const char* password = "";      // Password red wifi
const char* host = "";  // Server IP red wifi
const int   port = 80;            // Server Port
const int   watchdog = 5000;        // Watchdog frequency
unsigned long previousMillis = millis(); 
bool initialDateShown = false;
String today = "";
int ymd[] = {0, 0, 0};
String days[] = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};
int Raw       = A0;      //Analog channel A0 as used to measure temperature

DHT dht(dht_dpin, DHTTYPE); 
WiFiServer server(80);

WiFiUDP ntpUDP;         // set the ntp client
NTPClient timeClient(ntpUDP, "cl.pool.ntp.org", -14400, 60000);

void setup(void){ 
  dht.begin();                          //w
  Serial.begin(9600);
  delay(10);
  Serial.println("WiFi init ...");      //t y c
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");                   //t
  Serial.println("WiFi connected");  
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  Serial.println("Init RTC module..."); //c
  delay(2000);
  if (! rtc.begin()) {
    Serial.println("Couldn't find RTC");
    abort();
  }
  Serial.println("\n\nProyecto MITHumedad y Temperatura");
  Serial.println("Humedad, Temperatura del aire y Humedad suelo\n\n");
  delay(2000);
  timeClient.begin();                    //c
  timeClient.update();
  rtc.adjust(timeClient.getEpochTime());
  delay(2000);
  server.begin(); // Start the server   //w
  Serial.println("Server started");
  Serial.print("Use this URL to connect: ");// Print the IP address on serial monitor
  Serial.print("http://");    //URL IP to be typed in mobile/desktop browser
  Serial.print(WiFi.localIP());
  Serial.println("/");
  pinMode(D4,OUTPUT);                   //leds
  pinMode(D5,OUTPUT);
  pinMode(D6,OUTPUT);
  pinMode(D7,OUTPUT);
  pinMode(D8,OUTPUT);
}


// función hora actual y devuelve string hora formateada
String formattedTime(DateTime now) {
  String result = "";
  result = result + days[now.dayOfTheWeek()] + " ";
  result.concat(now.day());
  result.concat(" ");
  result.concat(now.month());
  result.concat(" ");
  result.concat(now.year());
  result.concat(" ");
  if(now.hour() < 10){
    result.concat("0");
  }
  result.concat(now.hour());
  result.concat(":");
  if(now.minute() < 10){
    result.concat("0");
  }
  result.concat(now.minute());
  result.concat(":");
  if(now.second() < 10){
    result.concat("0");
  }
  result.concat(now.second());
  return result;
}

// " "Fecha
String formatedDate(DateTime now) {
  String result = "";
  result = result + days[now.dayOfTheWeek()] + " ";
  result.concat(now.day());
  result.concat("-");
  result.concat(now.month());
  result.concat("-");
  result.concat(now.year());
  return result;
}


void loop() {
 
  DateTime now = rtc.now();
  if(!initialDateShown){
    today = formatedDate(now);
    initialDateShown = true;
    Serial.print(" Fecha = ");
    Serial.print(today);
  } else {
    if(now.hour() == 23 && now.minute() == 59 && now.second()== 59) {
      initialDateShown = false;
    }
  }
  WiFiClient client = server.available();
  float h =0.0;  //Nivel de humedad
  float t =0.0;  //Temperatura en grados centígrados
  float percentage = 0.0; // Cálculo del porcentaje de humedad
  float reading    = 0.0; //Lectura de humedad (analógico)

  h = dht.readHumidity();  
  t = dht.readTemperature();  
  reading = analogRead(Raw);           //Lectura de pin analógico por sensor de humedad del agua
  //percentage = (reading/1024) * 100; //Convertir en porcentaje
  Serial.println("  ");  
  Serial.print("Temperatura = ");
  Serial.print(t); 
  Serial.println("°C  ");
  Serial.print("Humedad aire = ");
  Serial.print(h);
  Serial.println("%  ");
  Serial.print("Moisture = ");
  Serial.println(reading);
  //Serial.println("%");
  Serial.print("Hora = ");
  String hora= formattedTime(now);
  Serial.println(hora);   
  Serial.println("  ");
  digitalWrite(D4,LOW);                //leds
  digitalWrite(D5,LOW);
  digitalWrite(D6,LOW);
  digitalWrite(D7,LOW);
  digitalWrite(D8,LOW);
  if(reading<200){                     //niveles leds
      digitalWrite(D4,HIGH);
    }else{
      if(reading < 400){
          digitalWrite(D5,HIGH);
        }else{
        if(reading < 600){
          digitalWrite(D6,HIGH);
        }else{
            if(reading < 800){
            digitalWrite(D7,HIGH);
            }else{
            digitalWrite(D8,HIGH);
                }
            }
        }
    } 
  client.println("HTTP/1.1 200 OK");// Devolver la respuesta
  client.println("Content-Type: text/html");
  client.println(""); 
  client.println("<!DOCTYPE HTML>");
  client.println("<html>");
  client.println("<h1 align=center>MIT Proyect</h1><br><br>");
  client.print("Temperature in Celsius =");
  client.println(t);
  client.println("<br>");
  client.print("Humidity =");
  client.println(h);
  client.print(" %");   
  client.println("<br>");  
  client.println();
  client.print("Moisture Level Percentage =");
  client.print(percentage);
  client.print("%");
  client.println("<br><br>");
  client.println("<a href=\"/Up=ON\"\"><button>Update = Temperature  Humidity Moisture Values</button></a><br />"); 
  client.println("</html>");
  delay(1);
  Serial.println("Client disonnected");
  Serial.println("");
  
    unsigned long currentMillis = millis();
    
  if ( currentMillis - previousMillis > watchdog ) {
    previousMillis = currentMillis;
    WiFiClient client;
  
    if (!client.connect(host, port)) {
      Serial.println("Fallo al conectar");
      return;
    }

    String url = "/mit/index.php?temp=";
    url += t;
    url += "&hum=";
    url += h;
    url += "&soil=";
    url += reading;
    //url += "&time=";
    //url += hora;
    
    client.print(String("GET ") + url + " HTTP/1.1\r\n" +// Enviamos petición al servidor
               "Host: " + host + "\r\n" + 
               "Connection: close\r\n\r\n");
    unsigned long timeout = millis();
    while (client.available() == 0) {
      if (millis() - timeout > 5000) {
        Serial.println(">>> Client Timeout !");
        client.stop();
        return;
      }
    }
      
    while(client.available()){ // Leemos la respuesta del servidor
      String line = client.readStringUntil('\r');
      Serial.print(line);
    }
  }
  delay(25000);
}
