import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

def fade():
  for number in range(100):
    led = 0
    time.sleep(0.0001)
    for px in pinlist:
      led += 1
      dc =  ((led * spacer) + i ) % 100
      if number > dc:
        GPIO.output(px,GPIO.HIGH)
      else:
        GPIO.output(px,GPIO.LOW)

pinlist = [7, 15, 29, 35, 33]
led_count = len(pinlist)
spacer = ( 100 / led_count )

for px in pinlist:
  GPIO.setup(px, GPIO.OUT)

i = 1
try:
  while True:
    i = i + 1
    fade()

except KeyboardInterrupt:
  pass

finally:
  GPIO.cleanup() # this ensures a clean exit

