from deplacement import Move
from motor import Motor
from esp_ble_uart import *
import time

nom = 'ESP32-ble-uart'
UUID_UART = '6E400001-B5A3-F393-E0A9-E50E24DCCA9E'
UUID_TX = '6E400003-B5A3-F393-E0A9-E50E24DCCA9E'
UUID_RX = '6E400002-B5A3-F393-E0A9-E50E24DCCA9E'
val_rx = "12"

uart = Bleuart(nom, UUID_UART, UUID_TX, UUID_RX)

moteur_1 = Motor(16, 17)
moteur_2 = Motor(18, 5)
moteur_3 = Motor(27, 14)
moteur_4 = Motor(26, 25)
movement = Move(16, 17, 18, 5, 14, 27, 26, 25)

def rcp_rx():
    global val_rx
    global dir
    val_rx = uart.read().decode().strip()
    print('sur rx:', val_rx)
    dir = val_rx

uart.irq(handler=rcp_rx)

while True:
    if dir == "davg":
        print("davg")
        movement.mov("davg")
    elif dir == "davd":
        print("davd")
        movement.mov("davd")
    elif dir == "av":
        print("av")
        movement.mov("av")
    elif dir == "ar":
        print("ar")
        movement.mov("ar")
    elif dir == "g":
        print("g")
        movement.mov("g")
    elif dir == "darg":
        print("darg")
        movement.mov("darg")
    elif dir == "dard":
        print("dard")
        movement.mov("dard")
    elif dir == "d":
        print("d")
        movement.mov("d")
    elif dir == "stop":
        print("stop")
        movement.mov("stop")
    elif dir == "rotad":
        print("rotad")
        movement.mov("rotad")
    elif dir == "rotag":
        print("rotag")
        movement.mov("rotag")
    else:
        print('No action')
