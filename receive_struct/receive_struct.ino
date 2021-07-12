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
#define numBytes 10
union {
  char bytes[numBytes];
  struct {
    // int in arduino are 2 bytes long
    uint16_t data[5];
  } unpacked;
} packet;

void readPacket() {
  while (Serial.available() < numBytes);
  // do nothing and wait if serial buffer doesn't have enough bytes to read
  Serial.readBytes(packet.bytes, numBytes);
  // read numBytes bytes from serial buffer and store them at a
  // union called “packet”
}

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(2000);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // the very important part of the sketch
  readPacket();

  blinkLed(packet.unpacked.data[0]);
  blinkLed(packet.unpacked.data[1]);
  blinkLed(packet.unpacked.data[2]);
  blinkLed(packet.unpacked.data[3]);
  blinkLed(packet.unpacked.data[4]);
  
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
