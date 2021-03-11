import machine, neopixel, time
np = neopixel.NeoPixel(machine.Pin(21),1)

def buzz():
    
    buzzer_pin=machine.Pin(18,machine.Pin.OUT)
    buzzer=machine.PWM(buzzer_pin)
    buzzer.freq(1027)
    buzzer.duty(500)
    time.sleep(0.5)
    buzzer.duty(0)
    time.sleep(1)
    buzzer.duty(500)
    time.sleep(1)
    buzzer.duty(0)    

Pir = machine.Pin(18, machine.Pin.IN,machine.Pin.PULL_UP)
def handle_interrupt(Pir):
    print(Pir.value())
    if Pir.value() == 1:
        print("Motion Detected")
        buzz()
        np[0]=(255,0,0)
        np.write()
        
    elif Pir.value() == 0:
        print("Motion Stopped")
        np[0]=(0,255,0)
        np.write()
        time.sleep(4)
        np[0]=(0,0,0)
        np.write()
        
        
Pir.irq(trigger = 3, handler = handle_interrupt)
time.sleep_ms(100)
