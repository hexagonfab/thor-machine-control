int signalPin = 10;

void setup() {
  pinMode(signalPin, OUTPUT);
  analogWrite(signalPin, 0);

  Serial.begin(9600);
}

void loop() {
  for (int i = 20; i < 90; i++) {
    analogWrite(signalPin, i);
    Serial.println(i);
    delay(10);
  }

  delay(1000);

  for (int i = 90; i > 20; i--) {
    analogWrite(signalPin, i);
    Serial.println(i);
    delay(10);
  }

  delay(1000);

//  analogWrite(signalPin, 100);
//  delay(3000);
//  analogWrite(signalPin, 0);
//  delay(3000);
}
