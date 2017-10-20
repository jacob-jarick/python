import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

def fade():
  for number in range(100):
    led = 1
    for px in pinlist:
      dc =  ((led * spacer) + i ) % 100
      if number > dc:
        GPIO.output(px,GPIO.HIGH)
      else:
        GPIO.output(px,GPIO.LOW)

      led += 1
      time.sleep(0.0001)

pinlist = [7, 15, 29, 35, 33]
led_count = len(pinlist)
spacer = ( 100 / led_count )
i = 1

for px in pinlist:
  GPIO.setup(px, GPIO.OUT)

try:
  while True:
    i = i + 1
    fade()

except KeyboardInterrupt:
  pass


finally:
  GPIO.cleanup() # this ensures a clean exit

