from djitellopy import Tello

# Uzdevums: Iziet trasi ar koda palidzību
# Noteikumi:
# - secīgi jaiziet cauri visiem vārtiem
# - jaapmeklē visas platformas
# - jaātgriezas atpakaļ
# - caur vārtiem drīkst līdot tikai taisni (ar kāmeru priekšā)

# Dokumentācija un piemēri
# https://github.com/damiafuentes/DJITelloPy/tree/master
# https://github.com/damiafuentes/DJITelloPy/blob/master/examples/simple.py

tello = Tello()

tello.connect()

tello.set_speed(15)
tello.takeoff()
tello.rotate_clockwise(180)
tello.move_forward(118)
tello.land()
tello.takeoff()
tello.rotate_counter_clockwise(90)
tello.move_left(10)
tello.move_forward(71)
tello.rotate_clockwise(90)
tello.move_forward(50)
tello.land()
tello.takeoff()
tello.rotate_clockwise(90)
tello.move_left(10)
tello.move_forward(72)
# 让每一架Tello单独执行不同的操作
tello.land()
tello.takeoff()
tello.rotate_clockwise(90)
tello.move_left(10)
tello.move_forward(169)
tello.land()

