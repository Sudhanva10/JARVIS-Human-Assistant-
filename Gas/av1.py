import time
import math
from gpiozero import MCP3008
adc1=MCP3008(channel=0)
sensorValue=0
x=0
for x in range(0,500):
    sensorValue= sensorValue + adc1.value
    x=x+1
sensorValue1=sensorValue/500
RSair=((3.3*10)/sensorValue1)-10
R0=RSair/9.9
while True:
    LPGm=-0.47
    LPGb=1.31
    sensorValue=adc1.value
    RSgas=((3.3*10)/sensorValue1)-10
    ratio1=(RSgas/R0)
    ratio=math.log10(ratio1)
    LPGratio=(ratio-LPGb)/LPGm
    LPGppm=math.pow(10,LPGratio)
    LPGperc=LPGppm/10000
    print(LPGperc,"LPG%")
    print(LPGppm,"LPGppm")
    time.sleep(0.5)