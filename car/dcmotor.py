import time

import Jetson.GPIO as GPIO


class DCMotor:
    def __init__(self, enable, in1, in2):
        self.enable = enable
        self.in1 = in1
        self.in2 = in2
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.enable, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.in1, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.in2, GPIO.OUT, initial=GPIO.LOW)

        GPIO.output(self.enable, GPIO.HIGH)
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)

    def forward(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)

    def backward(self):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)

    def stop(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)


def test_motor(motor):
    motor.forward()
    time.sleep(1)
    motor.backward()
    time.sleep(1)
    motor.stop()


if __name__ == "__main__":

    motor1 = DCMotor(40, 37, 35)
    motor2 = DCMotor(31, 29, 33)

    motor3 = DCMotor(23, 21, 19)
    motor4 = DCMotor(15, 13, 11)

    test_motor(motor4)
