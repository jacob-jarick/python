# written very quickly by jacob
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

pinlist = [7, 15, 29, 35, 33]
led_count = len(pinlist)
spacer = ( 100 / led_count )
i = 1

def fade():
  for number in range(100):
    led = 0
    for px in pinlist:
      led += 1
      dc =  ((led * spacer) + i ) % 100
      if number > dc:
        GPIO.output(px,GPIO.HIGH)
      else:
        GPIO.output(px,GPIO.LOW)

for px in pinlist:
  GPIO.setup(px, GPIO.OUT)

try:
  while True:
    i = i + 1

    for number in range(100):
      fade()

except KeyboardInterrupt:
  pass

finally:
  GPIO.cleanup() # this ensures a clean exit

