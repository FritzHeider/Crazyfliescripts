# Crazyfliescripts
Overview
This repository contains a collection of Python scripts for controlling the Crazyflie 2.0 drone using the Crazyradio PA USB dongle. These scripts demonstrate various capabilities from basic connection and battery checking to more advanced maneuvers and real-time keyboard controls.

Prerequisites
Before running these scripts, you need to have:

A Crazyflie 2.0 drone
A Crazyradio PA USB dongle
Python 3.6 or higher installed
cflib installed (Crazyflie library)
To install cflib, run:

bash
Download
Copy code
pip install cflib
For the real-time keyboard control script, you also need pygame:

bash
Download
Copy code
pip install pygame
Ensure your Crazyradio PA is plugged in and the Crazyflie is charged.

Script Descriptions
Basic Connection: Establishes a connection with the Crazyflie and keeps it alive until interrupted.
Battery Status Checker: Periodically logs the battery voltage to the console.
Takeoff and Hover: Commands the Crazyflie to take off, hover at a fixed height, and then land.
LED Control: Blinks the onboard LEDs in a set pattern.
Sensor Data Logger: Logs IMU data to a file at regular intervals.
Real-time Keyboard Control: Provides a GUI to control the drone with keyboard inputs in real-time. Displays current input values and system status on the screen.
Usage
Each script can be run independently based on the functionality you wish to test or demonstrate. To run a script, simply navigate to the script's directory in your terminal and execute:

bash
Download
Copy code
python <script_name>.py
Replace <script_name> with the name of the script you want to run.

Running the Real-time Keyboard Control Script
To use the real-time keyboard control:

Navigate to the script's directory.
Run:

python active.py
Use the arrow keys to control the drone's pitch and roll. Press the spacebar to cut thrust and ESC to quit the script.
Safety and Testing
Always test these scripts in an open area free from obstacles. Keep a safe distance from the drone while it is powered and possibly during flight tests. Ensure all safety measures are in place to prevent accidents or damage to the drone.

Support
For issues, questions, or contributions, please refer to the contact information or issue tracker on this repository's main page.
