import sys, argparse
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

def turnOnLED():
  GPIO.output(17, GPIO.HIGH)

def turnOffLED():
  GPIO.output(17, GPIO.LOW)


def main():
  print "Starting up program for controlling GPIO LED on RPi..."
  
  parser = argparse.ArgumentParser(description="Control GPIO LED on Raspberry Pi")

  group= parser.add_mutually_exclusive_group(required=True)
  group.add_argument('--on', action='store_true', help='turn ON the LED')
  group.add_argument('--off', action='store_false', help='turn OFF the LED')  

  args = parser.parse_args()
  
  if args.on:
    print "Turning ON LED..."
    turnOnLED()    
  else:
    print "Turning OFF LED..."
    turnOffLED()
  print "Closing..."

main()
GPIO.cleanup()
