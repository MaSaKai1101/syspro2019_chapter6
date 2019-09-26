#!/usr/bin/env python
# -*- coding:utf-8 -*-

import cgi
import cgitb    #display CGI error on browser
import time
import RPi.GPIO as GPIO


print('Content-type: text/html; charset=UTF-8\r\n')
print('Web Servo')

print('<form action="" method="post">')
print('Duty_value <input type="text" name="message">')
print('<input type="submit" name = "submit">')
print('</form>')

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

servo = GPIO.PWM(4, 50)

servo.start(0)

form = cgi.FieldStorage()
message = form.getvalue('message')
print(type(message))

for i in range(3):
	servo.ChangeDutyCycle(float(message))
	time.sleep(0.5)

servo.stop()
GPIO.cleanup()
