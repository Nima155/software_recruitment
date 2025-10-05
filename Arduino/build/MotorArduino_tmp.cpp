
void setup() {
	Serial.begin(19200);
}


void loop() {
	static const uint8_t INSTRUCTION_CODE = 0x1E;
	int sensorValue = analogRead(A2);
	if (sensorValue >= 0 && sensorValue <= 1023) {
		Serial.write(INSTRUCTION_CODE);
		uint16_t valM = map(sensorValue, 0, 1023, 818, 511);
		uint8_t arr[2] = {lowByte(valM), highByte(valM)};
		Serial.write(&arr[0], 2);
	}
	delay(100);
}

