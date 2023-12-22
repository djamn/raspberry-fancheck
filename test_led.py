import RPi.GPIO as GPIO
import time
print("Success1")

pin = 11
rounds = 3
sleeptime = 0.5
test=0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin,GPIO.HIGH)

for i in range(rounds):
	test += 1
	GPIO.output(pin,GPIO.HIGH)
	print("Enabled")
	time.sleep(sleeptime)
	GPIO.output(pin,GPIO.LOW)
	print(test)
	print("Disabled")
	time.sleep(sleeptime)
GPIO.cleanup()