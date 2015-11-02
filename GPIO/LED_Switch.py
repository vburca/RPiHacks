import time
import RPi.GPIO as GPIO

SWITCH_PIN = 17
LED_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)

def main():
  print "Starting up program for controlling GPIO LED on RPi with a switch..."
  
  state = False
    
  try:
    while True:
      # Change the state on each press of the switch based on its previous value
      if GPIO.input(SWITCH_PIN) == GPIO.HIGH:
        state = state % 2 == 0
        time.sleep(0.2)
      GPIO.output(LED_PIN, state)
  except KeyboardInterrupt:
    print "Finishing up..."


main()
GPIO.cleanup()
print "Bye!"
