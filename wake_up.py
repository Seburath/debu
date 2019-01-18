#Debu waking up code!
import time
from playsound import playsound

#init reaction <3
print("8                   ::d888,                           ,8:8.          8") 
print(":                   dY88888                           `' ::          8")
print(":                   8:8888                               `b          8") 
print(":                   Pd88P',...                     ,d888o.8          8") 
print(":                   :88'dd888888o.                d8888`88:          8") 
print(":                  ,:Y:d8888888888b             ,d88888:88:          8") 
print(":                  :::b88d888888888b.          ,d888888bY8b          8") 
print("                    b:P8;888888888888.        ,88888888888P          8") 
print("                    8:b88888888888888:        888888888888'          8") 
print("                    8:8.8888888888888:        Y8888888888P           8") 
print(",                   YP88d8888888888P'          ''888888'Y            8") 
print(":                   :bY8888P'''''''                     :            8") 
print(":                    8'8888'                            d            8") 
print(":                    :bY888,                           ,P            8") 
print(":                     Y,8888           d.  ,-         ,8'            8") 
print(":                     `8)888:           '            ,P'             8") 


playsound('sounds/bb8-11.mp3')
playsound('sounds/bb8-12.mp3')
playsound('sounds/bb8-13.mp3')

c = 0
while 1:
  time.sleep(60)
  playsound('sounds/bb8-03.mp3')
  c += 1
  print('ciclo: ' + str(c))
  if c == 45:
    playsound('sounds/bb8-04.mp3')
