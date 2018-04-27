import tello
import time
import network
from ssd1306 import SSD1306_I2C
from machine import Pin, I2C

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(b'iPal_TELLO')

i2c = I2C(scl=Pin(4), sda=Pin(5))
oled = SSD1306_I2C(128, 64, i2c)

attempt = 1
while not wifi.isconnected():
    oled.fill(0)
    oled.text('Connecting... {}'.format(attempt), 0, 0)
    oled.show()
    attempt += 1
    time.sleep(0.5)

drone = tello.Tello('192.168.10.2', 8888)

oled.fill(0)
drone.command('command')
oled.text('tello initialized!', 0, 0)
oled.show()
time.sleep(2)

oled.fill(0)
oled.text('takeoff', 0, 0)
drone.takeoff()
oled.show()
time.sleep(5)

oled.fill(0)
oled.text('flip left', 0, 0)
drone.flip('l')
oled.show()
time.sleep(5)

oled.fill(0)
oled.text('flip right', 0, 0)
drone.flip('r')
oled.show()
time.sleep(5)


oled.fill(0)
oled.text('landing...', 0, 0)
oled.show()
drone.land()
time.sleep(3)

oled.fill(0)
oled.text('landed :)', 0, 0)
oled.show()
