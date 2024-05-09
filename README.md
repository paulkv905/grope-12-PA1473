### Introduction
In this project we are programming an EV3 mindbricks robot. The general goal is to sort blocks of different colours into designated piles, with some additional specifications and requirements 
listed further down in this file.

### Getting started
To start developing in this project you will need a python editor, for example Visual Studio Code, and install the pybricks extension as well as pygame.  

### Building and running
The files in this repository are named based on their purpose. Any files that start with "older" are versions that are no longer in use, and any file starting with "current" are the files currently in use. Our main codes are divided into UI, single robot and multi robot. If you wish to use or run the UI, use the code called current_UI_unconnected.py. If you wish to run the program with only one robot, use current_single_robot.py, but if you wosh to run it in collaboration with another robot, use current_multi_robot.py.

When running this program on the robot, it will start by calibrating elevation, rotation and grip in the startup sequence. Please make sure there are no obstructions that may affect the calibration results. 
If the robot is used for the first time with the program, the pickup zones, sorting zones and dump zone will have to be set manually by the user, but after the initial setting they can be fetched from a save 
file for a faster setup process. To use a saved file, press the up button, to set manually, press the down button. 
When setting zones, use the robot buttons to adjust the crane horizontally and vertically to the desired location. Then confirm by pressing the center button. When all zones have been set, press the center 
button again to start the main program. From there on it will be sorting automatically.
If at any point you need to use the emergency stop function, press and hold the center button. The robot will start beeping to indicate the emergency stop being activated.
To pause, instead press and hold the down button. The robot will then vocally confirm that the pause has been activated. To unpause and resume, press the up button.
When connecting to another robot by bluetooth, please make sure the name of the robots are changed to correspond with the robots assigned letter to be more intuitive, as all robots have the same name as a default.

### User Stories Checklist
- [x] US_1: The robot should be able to pick up items of designated colours from a designated position. [1SP]
- [x] US_2: The robot should be equipped with colour sensors, and with the help of those sensors, be able to identify the colour of items and handle a maximum of three colours set by the user. [13SP]
- [x] US_3: The robot should be able to identify whether or not an item is present within the area.[5SP]
- [x] US_4: The robot should be equipped with speakers and, with the help of those speakers, be able to announce the colour of the item in English or Swedish.[1SP]
- [x] US_5: The robot should be able to drop off items at different specified locations based on the colour of the items. [3SP]
- [x] US_6: The robot should be able to pick up items from different levels of elevation within the robot’s reach. [8SP]
- [x] US_7: Any item identified as a colour other than the ones specified by the user should be ignored. [1SP]
- [x] US_8: The robot should be able to stay within a designated marked area. [0SP]
- [x] US_9: The robot should not drop the item from an elevated altitude. [2SP]
- [x] US_10: The process including identifying the colour of an item and dropping it off within a designated area should not exceed 5 seconds. [2SP]
- [x] US_11: If the robot does not find any item to sort it should go into an idle mode for 1-2 minutes before searching again. [3SP]
- [ ] US_12: Easily change the schedule of robot pickup task (absolute time). [13SP]
- [x] US_13: The robot should be able to work in tandem with another robot without obstructions.[34SP]
- [x] US_14: The user should easily be able to manually set locations and height of one pickup zone and three drop off-zones.[3SP]
- [x] US_15: Emergency stop button (terminates as it is, does not drop the item if held). [5SP]
- [ ] US_16: The robot should be able to pick up items from a rolling belt [34SP]
- [x] US_17: Pause button which stops the program then resumes from the same spot [13SP]
- [ ] US_18: Dashboard to configure robot program and start tasks on demand [21SP]

### Note on the User Stories Checklist
The UI dashboard for US_18 is developed but is yet to be connected with the robot program, hence making it unfinished.
THe absolute time schedule of US_12 is planned to connect with the UI dashboard, and is not finished due to the connecting issue in US_18.
