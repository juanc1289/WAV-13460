#!/usr/bin/python
# Filename: text.py
import serial
import time
ser = serial.Serial("/dev/ttyS0",115200)
W_buff = [b"AT\r\n", b"AT+CMGF=1\r\n", b"AT+CMGS=\"0477560148\"\r\n",b"helloworld"]
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
			#if data.count("O") > 0 and data.count("K") > 0 and num < 3:	# the string have ok
			if num < 3:
				time.sleep(1)
				ser.write(W_buff[num+1])
			#if num == 3 and data.count(">") > 0:
			if num == 2:
				#print W_buff[4]
				time.sleep(0.5)
				ser.write(W_buff[3])
				ser.write(b"\x1a\r\n")# 0x1a : send   0x1b : Cancel send
			num =num +1
			data = ""
except KeyboardInterrupt:
	if ser != None:
		ser.close()
