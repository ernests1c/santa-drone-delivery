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
tello.takeoff()

tello.set_speed(20)
tello.move_up(75)
tello.rotate_clockwise(180)
tello.move_forward(122)
tello.move_down(75)
tello.move_up(75)
tello.rotate_counter_clockwise(90)
tello.move_forward(75)
tello.rotate_clockwise(90)
tello.move_forward(64)
tello.move_down(75)
tello.move_up(75)
tello.rotate_clockwise(90)
tello.move_forward(75)
# 让每一架Tello单独执行不同的操作
tello.rotate_clockwise(360)
tello.rotate_counter_clockwise(360)
tello.move_down(75)
tello.land()
