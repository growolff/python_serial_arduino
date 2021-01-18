/*
 * by Gonzalo Olave
 * license CC zero universal
 * 
 * receive data structure from serial bus and blinks with function blinkLed()
 * 
 * modify for your own purposes
 * 
*/

// define data structure
// check data types here https://learn.sparkfun.com/tutorials/data-types-in-arduino/defining-data-types
struct machine {
  // int in arduino are 2 bytes long
  int d1;
  int d2;
  int d3;
  int d4;
};

struct machine MK1 = {0, 0, 0, 0};
int size_struct = sizeof(struct machine);

bool receive(machine* table)
{
  return (Serial.readBytes((char*)table, size_struct) == size_struct);
}

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // the very important part of the sketch
  if(receive(&MK1)) delay(100);

  blinkLed(MK1.d1);
  blinkLed(MK1.d2);
  blinkLed(MK1.d3);
  blinkLed(MK1.d4);
}

void blinkLed(int t) {
  digitalWrite(13, HIGH);
  delay(t/2);
  digitalWrite(13, LOW);
  delay(t/2);
  digitalWrite(13, HIGH);
  delay(t/2);
  digitalWrite(13, LOW);
  delay(t/2);
}
