from pyfirmata import Arduino, util
import time
from src.utils import map
board = Arduino("/dev/ttyACM1")

motor_e = board.get_pin("d:3:s")
motor_w = board.get_pin("d:5:s")
motor_n = board.get_pin("d:6:s")
motor_s = board.get_pin("d:9:s")

potential = board.get_pin("a:0:i")

it = util.Iterator(board)
it.start()


while True:
    pot_value = potential.read()
    if pot_value:
        mapped = int(map(pot_value))
        motor_e.write(mapped)
        print(pot_value)
        time.sleep(0.1)
