import sys, time
from inventorhatmini import InventorHATMini, MOTOR_A
from ioexpander.common import NORMAL_DIR, REVERSED_DIR

board = InventorHATMini(init_leds=False)
motor = board.motors[MOTOR_A]
motor.enable()

def down(duration):
    motor.direction(REVERSED_DIR)
    motor.speed(0.95)
    time.sleep(duration)
    motor.stop()

def up(duration):
    motor.direction(NORMAL_DIR)
    motor.speed(0.95)
    time.sleep(duration)
    motor.coast()
    motor.stop()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("USAGE: python3 camera-up-down.py up <motor speed [0.0-1.0]> <duration (sec)>")
        print("USAGE: python3 camera-up-down.py down <motor speed [0.0-1.0]> <duration (sec)>")
    else:
        if sys.argv[1] == "up":
            up( float(sys.argv[2]) )
        elif sys.argv[1] == "down":
            down( float(sys.argv[2]) )
        else:
            print("USAGE: python3 camera-up-down.py up <motor speed [0.0-1.0]> <duration (sec)>")
            print("USAGE: python3 camera-up-down.py down <motor speed [0.0-1.0]> <duration (sec)>")
    motor.disable()

