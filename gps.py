#!/usr/bin/python
# Filename: text.py
import serial
import time
import sys
ser = serial.Serial("/dev/ttyS0",115200)
#ser = serial.Serial("/dev/serial0",115200)
#ser = serial.Serial("/dev/ttyAMA0",115200)

W_buff = [b"AT+CGNSPWR=1\r\n", b"AT+CGNSSEQ=\"RMC\"\r\n", b"AT+CGNSINF\r\n", b"AT+CGNSURC=2\r\n",b"AT+CGNSTST=1\r\n"]
ser.write(W_buff[0])
ser.flushInput()
data = ""
num = 0

try:
	while True:
		#print ser.inWaiting()
		while ser.inWaiting() > 0:
			data += ser.read(ser.inWaiting()).decode()
		if data != "":
			print(data)
			if  num < 4:	# the string have ok
				print(num)
				time.sleep(0.5)
				ser.write(W_buff[num+1])
				num =num +1
			if num == 4:
				time.sleep(0.5)
				ser.write(W_buff[4])
			data = ""
except KeyboardInterrupt:
	if ser != None:
		ser.close()
		
