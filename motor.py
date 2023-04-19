# déplacement holonome
# https://www.raspberryme.com/micropython-gestionnaire-wi-fi-avec-esp32-et-esp8266/

import machine

class Motor:

    def __init__(self, pin1, pin2):
        self.pin1 = machine.Pin(pin1, machine.Pin.OUT)
        self.pin2 = machine.Pin(pin2, machine.Pin.OUT)
        self.pin1.value(0)
        self.pin2.value(0)
        self.vitesse = 1000
        self.speed = machine.PWM(machine.Pin(pin1))
        self.speed.freq(self.vitesse)
