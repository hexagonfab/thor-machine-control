/*
 * Control solenoid motion based on external commands 
 * from computer.
 * 
 * Written by Lukas Vasadi in April 2021
 */

int signalPin = 10;
char command;
bool motorsAtPosition = false;
int motorX;
int motorY;

bool checkMotorStates() {
  motorX = digitalRead(11);
  Serial.print("motorX: "); Serial.println(motorX);
  motorY = digitalRead(12);
  Serial.print("motorY: "); Serial.println(motorY);
  if (!motorX && !motorY) return true;
  else return false;
}

void setup() {
  pinMode(signalPin, OUTPUT); // Set signalPin as OUTPUT
  analogWrite(signalPin, 0);  // Initialize signalPin

  Serial.begin(9600);
}

void loop() {
  // Wait for command from software
  while (!Serial.available()); // Wait for input

  command = Serial.read(); // Read serial buffer

  // If the user wants to deploy the solenoid...
  if (command == 'D') {
    // First check motor states
//    while (!motorsAtPosition) {
//      motorsAtPosition = checkMotorStates();
//    }
    for (int i = 18; i < 81; i++) {
      analogWrite(signalPin, i);
//      Serial.println(i);
      delay(10);
    }
//    motorsAtPosition = false; // Reinitialize motorsAtPosition/
  }

  // If the user wants to raise the solenoid...
  else if (command == 'U') {
    for (int i = 80; i > 17; i--) {
      analogWrite(signalPin, i);
//      Serial.println(i);
      delay(10);
    }
  }
}
