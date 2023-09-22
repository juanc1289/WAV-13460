import serial
import time 

phone = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=2.0)

message='AT+CGNSPWR=1\r\n'
message_utf= message.encode(encoding='utf-8', errors = 'strict')

phone.write(message_utf)
result=phone.read(100)
print(result)
#print('message 1: ',message_utf)

message='AT+CGNSINF\r\n'
message_utf= message.encode(encoding='utf-8', errors = 'strict')

phone.write(message_utf)
result=phone.read(100)
print(result)


message='AT+CMGF=1\r\n'
message_utf= message.encode(encoding='utf-8', errors = 'strict')

phone.write(message_utf)
result=phone.read(100)
print(result)

message='AT+CMGR=1\r\n'
message_utf= message.encode(encoding='utf-8', errors = 'strict')

phone.write(message_utf)
result=phone.read(100)
print(result)


message='AT+CMGS="+32477560148"\r\n'
message_utf= message.encode(encoding='utf-8', errors = 'strict')

phone.write(message_utf)
result=phone.read(100)
print(result)

message='hello world \032'
message_utf= message.encode(encoding='utf-8', errors = 'strict')

phone.write(message_utf)
result=phone.read(100)
print(result)

