from integracao import *
io = IO()
while True:
    listLED = [i for i in range(18) if io.get_SW(i)]
    io.put_ar_LD(listLED, LED_R)