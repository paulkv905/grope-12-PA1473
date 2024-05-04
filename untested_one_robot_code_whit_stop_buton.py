#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (
    Motor,
    TouchSensor,
    ColorSensor,
    InfraredSensor,
    UltrasonicSensor,
    GyroSensor,
)
from pybricks.parameters import Port, Stop, Direction, Button, Color
import time

ev3 = EV3Brick()
motor1 = Motor(Port.C)
rotation = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])
elevation = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 40])
gripper = Motor(Port.A)
touchsensor = TouchSensor(Port.S1)
colorSensor = ColorSensor(Port.S2)


# the emergansy stop buten is plased in evry uthjer row 
def emergensy_stop():
    center_button = Button.CENTER in ev3.buttons.pressed()
    if center_button:
        while True:
            elevation.hold()
            rotation.hold()
            gripper.hold()
            ev3.speaker.beep()
            time.sleep(0.1)


# calebrating the zero position 
def reset():
    emergensy_stop()
    gripper.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
    emergensy_stop()
    ev3.screen.clear()
    emergensy_stop()
    ev3.screen.draw_text(10, 10, "Make way.")
    emergensy_stop()
    ev3.screen.clear()
    emergensy_stop()
    ev3.screen.draw_text(10, 10, "Calibrating")
    emergensy_stop()
    elevation.run_until_stalled(-120, duty_limit=15, then=Stop.HOLD)
    emergensy_stop()
    while True:
        emergensy_stop()
        elevation.run(10)
        emergensy_stop()
        if colorSensor.reflection() == 0:
            emergensy_stop()
            time.sleep(1)
            emergensy_stop()
            elevation.run(-20)
            emergensy_stop()
            time.sleep(1)
            emergensy_stop()
            elevation.reset_angle(0)
            emergensy_stop()
            elevation.hold()
            emergensy_stop()
            break
    while True:
        emergensy_stop()
        rotation.run(-20)
        emergensy_stop()
        if touchsensor.pressed():
            emergensy_stop()
            ev3.speaker.beep()
            emergensy_stop()
            break
    emergensy_stop()
    rotation.reset_angle(0)
    emergensy_stop()
    gripper.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
    emergensy_stop()
    gripper.reset_angle(0)
    emergensy_stop()
    gripper.run_target(500, -90)
    emergensy_stop()
    ev3.screen.clear()
    emergensy_stop()
    ev3.screen.draw_text(10, 10, "Calibration complete.")
    emergensy_stop()


# gows to the pickup zone
def go_to_0(zone_info_matrix):
    emergensy_stop()
    pickup_zone = zone_info_matrix[0]
    emergensy_stop()
    time.sleep(0.1)
    emergensy_stop()
    time.sleep(0.1)
    emergensy_stop()
    rotation.run_target(500, pickup_zone[0])
    emergensy_stop()
    rotation.hold()
    emergensy_stop()
    elevation.run_target(500, pickup_zone[1])
    emergensy_stop()
    elevation.hold()
    emergensy_stop()
    gripper.run_target(500, 0)
    emergensy_stop()
    gripper.hold()
    emergensy_stop()


# Assigns 1 pickup 3 drop of and 1 dump zones and saves them in zone_info_matrix
def set_drop_off_zones():
    emergensy_stop()
    ev3.screen.clear()
    emergensy_stop()
    ev3.screen.draw_text(
        10,
        10,
        "Assign 1 pickup 3 drop of and 1 dump zone",
    )
    emergensy_stop()
    rotation_temp_int = 0
    emergensy_stop()
    elevation_temp_int = 0
    emergensy_stop()
    zone_temp_int = 0
    emergensy_stop()
    zone_info_matrix = []
    emergensy_stop()

    while True:
        time.sleep(0.1)
        center_button = Button.CENTER in ev3.buttons.pressed()
        up_button = Button.UP in ev3.buttons.pressed()
        down_button = Button.DOWN in ev3.buttons.pressed()
        left_button = Button.LEFT in ev3.buttons.pressed()
        right_button = Button.RIGHT in ev3.buttons.pressed()
        rotation.run_target(10, rotation_temp_int)
        rotation.hold()
        elevation.run_target(10, elevation_temp_int)
        elevation.hold()

        if left_button and rotation_temp_int < 250:
            rotation_temp_int += 1
        elif right_button and rotation_temp_int > 0:
            rotation_temp_int -= 1
        elif up_button and rotation_temp_int < 250:
            elevation_temp_int += 1
        elif down_button and rotation_temp_int > 0:
            elevation_temp_int -= 1
        elif center_button:
            if zone_temp_int == 5:
                return zone_info_matrix
            else:
                rotation_int = rotation_temp_int
                elevation_int = elevation_temp_int
                zone_info_matrix.append([rotation_int, elevation_int])
                zone_temp_int += 1
                time.sleep(0.1)
                ev3.screen.clear()
                ev3.screen.draw_text(10, 10, "Drop off zone set.")
                time.sleep(1)


# moving to the given zone and adjusting elevation sow it doesn't run into the old blocks
def go_to_the_zones(zone_info_matrix, i=1):
    emergensy_stop()
    rotation1 = zone_info_matrix[i][0]
    emergensy_stop()
    elevation1 = zone_info_matrix[i][1]
    emergensy_stop()
    rotation.run_target(500, rotation1)
    emergensy_stop()
    elevation.run_until_stalled(-200, then=Stop.HOLD, duty_limit=15)
    emergensy_stop()
    time.sleep(0.1)
    emergensy_stop()
    gripper.run_target(500, -90)
    emergensy_stop()
    time.sleep(0.1)
    emergensy_stop()
    elevation.run_target(200, elevation1 + 50)
    emergensy_stop()
    time.sleep(0.1)
    emergensy_stop()
    zone_info_matrix[i][1] = zone_info_matrix[i][1] + 10
    emergensy_stop()
    return zone_info_matrix


# staying idle for 10 seconds then running the main code again
def idle_mode():
    emergensy_stop()
    ev3.screen.clear()
    emergensy_stop()
    ev3.screen.draw_text(10, 10, "bravo 6 going dark")
    emergensy_stop()
    elevation.run_until_stalled(500, then=Stop.HOLD, duty_limit=25)
    emergensy_stop()
    for i in range(1):
        time.sleep(1)
        emergensy_stop()
    emergensy_stop()
    ev3.screen.clear()
    emergensy_stop()
    ev3.screen.draw_text(10, 10, "resuming work")
    emergensy_stop()


# the robot picking up the block, writing its colour and returning what zone to put the block in
def pick_up_block():
    emergensy_stop()
    if gripper.angle() > 0:
        emergensy_stop()
        idle_mode()
    else:
        emergensy_stop()
        time.sleep(0.1)
        emergensy_stop()
        elevation.run_target(500, 5)
        emergensy_stop()
        elevation.hold()
        emergensy_stop()
        time.sleep(0.1)
        emergensy_stop()

        if colorSensor.color() == Color.RED:
            emergensy_stop()
            ev3.screen.clear()
            emergensy_stop()
            ev3.screen.draw_text(10, 10, "red")
            emergensy_stop()
            ev3.speaker.say("red")
            emergensy_stop()
            return 1
        elif colorSensor.color() == Color.GREEN:
            emergensy_stop()
            ev3.screen.clear()
            emergensy_stop()
            ev3.screen.draw_text(10, 10, "green")
            emergensy_stop()
            ev3.speaker.say("green")
            emergensy_stop()
            return 2
        elif colorSensor.color() == Color.BLUE:
            emergensy_stop()
            ev3.screen.clear()
            emergensy_stop()
            ev3.screen.draw_text(10, 10, "blue")
            emergensy_stop()
            ev3.speaker.say("blue")
            emergensy_stop()
            return 3
        else:
            ev3.screen.clear()
            emergensy_stop()
            ev3.screen.draw_text(10, 10, "wrong")
            emergensy_stop()
            ev3.speaker.say("undisered color")
            emergensy_stop()
            return 4


# asks if the robot should use the pre-assigned drop-off zones or if it should be reassigned manually
def set_zones_or_load():
    emergensy_stop()
    ev3.screen.clear()
    emergensy_stop()
    ev3.screen.draw_text(10, 10, "up to load")
    emergensy_stop()
    ev3.screen.draw_text(10, 25, "down for manually")
    emergensy_stop()
    while True:
        emergensy_stop()
        up_button = Button.UP in ev3.buttons.pressed()
        emergensy_stop()
        down_button = Button.DOWN in ev3.buttons.pressed()
        emergensy_stop()
        if up_button:
            emergensy_stop()
            ev3.screen.clear()
            emergensy_stop()
            ev3.screen.draw_text(10, 10, "Loading file")
            emergensy_stop()
            return True
        elif down_button:
            emergensy_stop()
            ev3.screen.clear()
            emergensy_stop()
            ev3.screen.draw_text(10, 10, "Manual mode")
            emergensy_stop()
            return False


# the main code that loops for infinity
def main_running_code(zone_info_matrix):
    emergensy_stop()
    while True:
        emergensy_stop()
        go_to_0(zone_info_matrix)
        emergensy_stop()
        time.sleep(0.1)
        emergensy_stop()
        drop_of_zone_index = pick_up_block()
        emergensy_stop()
        zone_info_matrix = go_to_the_zones(zone_info_matrix, drop_of_zone_index)
        emergensy_stop()


# calibration/zeroing and starting sequence (only happens once per run)
def start_upp_sequence():

    ev3.speaker.beep()
    time.sleep(0.1)
    ev3.speaker.beep()
    ev3.screen.clear()
    ev3.screen.draw_text(10, 10, "Starting up.")
    reset()
    ev3.speaker.beep()
    time.sleep(0.1)
    ev3.speaker.beep()
    time.sleep(0.1)

    if set_zones_or_load():
        try:
            with open("saved_location2.txt") as save_file:
                zone_info_matrix = json.load(save_file)
        except OSError as error_mesage:
            print(error_mesage)
            ev3.screen.clear()
            ev3.screen.draw_text(10, 10, "File not found. Manual setting started.")
            zone_info_matrix = set_drop_off_zones()
            with open("saved_location2.txt", "w") as save_file:
                json.dump(zone_info_matrix, save_file)

    else:
        zone_info_matrix = set_drop_off_zones()
        with open("saved_location2.txt", "w") as save_file:
            json.dump(zone_info_matrix, save_file)
    go_to_0(zone_info_matrix)
    main_running_code(zone_info_matrix)


# start program
# print(colorSensor.rgb())
start_upp_sequence()
