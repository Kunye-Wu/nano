\* What is the difference between a computer board vs flight controller?

Computer Board: Contains complex programs - computational intensive
operations Deals with high level tasks like image processing and machine
learning Receives power from separate battery Takes in sensors such as
camera to do cv Runs linux

Flight Controller: Receives information from sensors Receives power from
main battery Controls esc -\> brushless motors Only responsible for
flight Focuses on real time flight control and stability

\* What operating systems, software, firmware, and middleware do each
run? Computer Board: \* Operating system: Linux, Ubuntu \* Software:
Tensorflow \* Firmware: a microcode or program embedded into memory of
hardware devices to help them operate \* Acts as translation between
machine instructions and circuit level of computer \* Middleware:
MAVROS2 Flight Controller: Pixhawk 6C Mini \* Operating system: NuttX \*
Software: PX4, ArduPilot \* Firmware: a microcode or program that is
embedded into the memory of hardware devices to help them operate \*
Acts as translation between machine instructions and circuit level of
computer \* Middleware: ROS2

\* How do the two communicate with each other? They can communicate
through Mavlink Protocol, where the Compute Board sends high level
commands and processed sensor data to the Flight Controller. And the
Flight Controller sends sensor readings and status updates to Computer
Board

\* Which sensors are processed by which processor? Cameras/LIDAR/etc. -
Perception Nodes, Raspberry Pi IMU, GPS, low-level sensors - Flight
Controller

\* What are NuttX, uORB and Mavlink? NuttX: Real time operating system
(RTOS) on the Flight Controller uORB: Facilitates communication within
the flight controller Mavlink: A lightweight, open-source communication
protocol designed for unmanned vehicles, such as drones.
