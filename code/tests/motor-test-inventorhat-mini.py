import time
from inventorhatmini import InventorHATMini, MOTOR_A
from ioexpander.common import NORMAL_DIR, REVERSED_DIR

board = InventorHATMini(init_leds=False)
m = board.motors[MOTOR_A]
m.enable()

m.speed(0.5)
time.sleep(2)
m.stop()
time.sleep(1)

m.direction(REVERSED_DIR)
m.speed(0.5)
time.sleep(2)
m.stop()


