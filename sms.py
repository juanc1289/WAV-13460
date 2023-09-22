import serial
import time 

phone = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=1.0)

message1='AT+CGNSPWR=1\r\n'
messageutf1= message1.encode(encoding='utf-8', errors = 'strict')

phone.write(messageutf1)
result=phone.read(100)
print(result)

message2='AT+CGNSINF\r\n'
messageutf2= message2.encode(encoding='utf-8', errors = 'strict')

phone.write(messageutf2)
result=phone.read(100)
print(result)
