import pycom
from machine import SPI,UART
import time


temp = SPI(0, mode=SPI.MASTER, baudrate=9600, polarity=0, phase=0)

while True :
    x=temp.read(2)
    print(x)
    try:
        #bits=x.decode()
        print('bits: ',bin(x))
    except:
        pass
    time.sleep(0.1)
