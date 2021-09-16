
#include <Servo.h>

#define SERVO_PIN   3

Servo motor;

void setup() {
  motor.attach(SERVO_PIN);
  motor.write(90);
}

void loop() {
  
    motor.write(90);
    delay(2000);
    motor.write(180);
    delay(2000);
    motor.write(0);
    delay(2000);

}
