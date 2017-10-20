import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)

p = GPIO.PWM(7, 50)
p2 = GPIO.PWM(15, 50)
p3 = GPIO.PWM(29, 50)
p4 = GPIO.PWM(35, 50)
p5 = GPIO.PWM(33, 50)

pinlist = [p, p2, p3, p4, p5]

led_count = 5
i = 1


for px in pinlist:
	px.start(0)

try:
	while True:
		i = i + 1
		led = 0
		temp = ( 100 / led_count )

		for px in pinlist:
			dc =  ((led * temp) + i ) % 100
			led += 1

		time.sleep(0.003)

except KeyboardInterrupt:
	pass

for px in pinlist:
	px.stop(0)

finally:

	GPIO.cleanup() # this ensures a clean exit
