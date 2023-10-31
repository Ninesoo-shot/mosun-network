import serial
import pyfirmata
import time

port = '/dev/ttyACM0'
board = pyfirmata.Arduino(port)
brate = 57600

board.digital[7].mode = pyfirmata.OUTPUT

seri = serial.Serial(port, baudrate = brate, timeout = None)
print(seri.name)

seri.write(b'\x0101')

a = 1
while a:
    if seri.in_waiting != 0 :
        content = seri.readline()
        print(content.decode())
        a = 0

while 1:
    board.digital[7].write(1)
    time.sleep(1)

    board.digital[7].write(0)
    time.sleep(1)
