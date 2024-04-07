#!/usr/bin/env pybricks-micropython
import time
import json
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
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# set all the robots ports
ev3 = EV3Brick()
motor1 = Motor(Port.C)
rotation = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])
elevation = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 40])
gripper = Motor(Port.A)
touchsensor = TouchSensor(Port.S1)
colorSensor = ColorSensor(Port.S2)


# define zero position
def reset():
    gripper.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
    ev3.speaker.say("Make way.")
    time.sleep(0.1)
    ev3.speaker.say("Calibrating")
    time.sleep(0.1)
    elevation.run_until_stalled(-120, duty_limit=15, then=Stop.HOLD)
    while True:
        elevation.run(15)
        if colorSensor.reflection() == 0:
            elevation.run(-10)
            time.sleep(1)
            elevation.reset_angle(0)
            elevation.hold()
            break
    time.sleep(0.1)
    while True:
        rotation.run(-10)
        if touchsensor.pressed():
            ev3.speaker.beep()
            break
    rotation.reset_angle(0)
    time.sleep(0.1)
    gripper.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
    gripper.reset_angle(0)
    gripper.run_target(500, -90)
    time.sleep(0.1)
    ev3.speaker.say("Calibration complete.")
    time.sleep(0.1)


# go to zero
def go_to_0():
    time.sleep(0.1)
    ev3.speaker.say("Returning to zero.")
    time.sleep(0.1)
    rotation.run_target(500, 0)
    rotation.hold()
    elevation.run_target(500, 0)
    elevation.hold()
    gripper.run_target(500, 0)
    gripper.hold()


# set drop off zones
def set_drop_off_zones():
    ev3.speaker.say(
        "Assign 3 drop of zones. Use the arrow keys to align the crane with the drop of zone. Then press the center button to select."
    )
    rotation_temp_int = 0
    elevation_temp_int = 0
    zone_temp_int = 0
    zone_info_matrix = []

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
            if zone_temp_int == 3:
                return zone_info_matrix
            else:
                rotation_int = rotation_temp_int
                elevation_int = elevation_temp_int
                zone_info_matrix.append([rotation_int, elevation_int])
                zone_temp_int += 1
                time.sleep(0.1)
                ev3.speaker.say("Drop off zone set.")
                time.sleep(1)


# moving to the given zone and adjusting elevation so it doesn't run into the old blocks
def go_to_the_zones(zone_info_matrix, i=0):
    text = str("Going to zone ", i)
    ev3.speaker.say(text)
    rotation1 = zone_info_matrix[i][0]
    elevation1 = zone_info_matrix[i][1]
    rotation.run_target(500, rotation1)
    elevation.run_until_stalled(-500, then=Stop.HOLD, duty_limit=15)
    time.sleep(0.1)
    gripper.run_target(500, -90)
    time.sleep(0.1)
    elevation.run_target(500, elevation1 + 50)
    time.sleep(0.1)
    zone_info_matrix[i][1] = zone_info_matrix[i][1] + 10
    return zone_info_matrix


# staying idle for 10 seconds then running the main code again
def idle_mode():
    go_to_0()
    time.sleep(10)


# the robot picking up the block, writing its colour and returning what zone to put the block in
def pick_up_block():
    while True:
        elevation.run_target(500, 0)
        rotation.run_target(500, 0)
        gripper.run_target(500, -90)
        time.sleep(0.1)
        elevation.run_until_stalled(-200, then=Stop.COAST, duty_limit=25)
        time.sleep(0.1)
        gripper.run_until_stalled(200, then=Stop.HOLD, duty_limit=100)
        time.sleep(0.1)
        elevation.run_target(500, 5)
        elevation.hold()
        time.sleep(2)
        r, g, b = colorSensor.rgb()

        if colorSensor.color() == Color.RED:
            ev3.speaker.say("The block is red")
            return 0
        elif colorSensor.color() == Color.GREEN:
            ev3.speaker.say("The block is green")
            return 1
        elif colorSensor.color() == Color.BLUE:
            ev3.speaker.say("The block is blue")
            return 2
        else:
            ev3.speaker.say("no desired block detected")
            gripper.run_target(500, -90)
            idle_mode()


# asks if the robot should use the pre-assigned drop off zones or if it should be reassigned manually
def set_zones_or_load():
    ev3.speaker.say(
        "Press the up button to load saved drop off locations, or press the down button to manually set locations"
    )
    while True:
        up_button = Button.UP in ev3.buttons.pressed()
        down_button = Button.DOWN in ev3.buttons.pressed()
        if up_button:
            ev3.speaker.say("Loading file")
            return True
        elif down_button:
            ev3.speaker.say("Manual mode")
            return False


# the main code that loops for infinity
def main_running_code(zone_info_matrix):
    while True:
        go_to_0()
        time.sleep(0.1)
        ev3.speaker.say("Picking up block.")
        time.sleep(1)
        drop_of_zone_index = pick_up_block()
        zone_info_matrix = go_to_the_zones(zone_info_matrix, drop_of_zone_index)


# calibration/zeroing and starting sequence (only happens once per run)
def start_upp_sequence():
    ev3.speaker.beep()
    time.sleep(0.1)
    ev3.speaker.beep()
    ev3.speaker.say("Starting up.")
    reset()
    ev3.speaker.beep()
    time.sleep(0.1)
    ev3.speaker.beep()
    go_to_0()
    time.sleep(0.1)

    if set_zones_or_load():
        try:
            with open("saved_location1.txt") as save_file:
                zone_info_matrix = json.load(save_file)
        except:
            ev3.speaker.say("File not found. Manual setting started.")
            zone_info_matrix = set_drop_off_zones()
            with open("saved_location1.txt", "w") as save_file:
                json.dump(zone_info_matrix, save_file)

    else:
        zone_info_matrix = set_drop_off_zones()
        with open("saved_location1.txt", "w") as save_file:
            json.dump(zone_info_matrix, save_file)

    main_running_code(zone_info_matrix)


# start program
# print(colorSensor.rgb())
start_upp_sequence()
