import serial
import time 

phone = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=1.0)

phone.write(b'AT+CGNSPWR=1\r\n')
result=phone.read(100)
print(result)

phone.write(bytes('AT+CGNSINF\r\n','utf-8'))
result=phone.read(100)
print(result)
