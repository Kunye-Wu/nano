What are some of the differences between a research and development
drone vs other \"commercial\" or \"toy\" drones? Quality and Durability:
\* R&D Drones: Built with higher quality materials for durability and
reliability in various testing environments. They often have advanced
sensors and components for precise data collection. \* Commercial/Toy
Drones: Generally made with cost-effective materials, focusing on
affordability and ease of use. They might lack advanced features and
robustness. Autonomy and Software: \* R&D Drones: Often feature advanced
autonomy and software for specific research applications, including AI
and machine learning capabilities. Advanced sensors and able to
accomplish more complex tasks \* Commercial/Toy Drones: Focus on
user-friendly software with limited autonomy, usually controlled via
remote or smartphone apps.

What are some current applications of autonomous drones? Can you think
of any future applications as technology improves (e.g. faster, smaller,
more efficient computers)?

\* Some of the current applications of autonomous drones include
autonomous delivery, landscape photography, planting farms, and human or
animal rescue in places that are hard for humans to enter. Some of the
future applications with smarter computers and more advanced technology
are delivering medical supplies, food, and water to disaster-stricken or
remote areas quickly, monitoring the public spaces with advanced sensors
and AI to detect suspicious activities, and assisting law enforcement in
real-time, tracking wildlife populations and environmental changes to
provide more data to scientists to understand the changes to our planet,
autonomously inspecting and monitoring infrastructure such as bridges,
power lines, and pipelines for maintenance and early detection of
issues, providing 3D mapping for city planning to prevent issues such as
traffic jams, providing materials and supplies to troops in remote or
dangerous locations.

Describe the difference between the Compute Board and Flight Controller.
What purposes do each serve? What operating systems do each run? \*
Computer Board: Contains complex programs - computational intensive
operations \* Deals with high level tasks like image processing and
machine learning \* Receives power from separate battery \* Takes in
sensors such as camera to do cv \* Runs linux: \* Receives information
from sensors \* Receives power from main battery \* Controls esc -\>
brushless motors \* Only responsible for flight \* Focuses on real time
flight control and stability \* Compute Board uses Linux, Ubuntu \*
Flight Controller uses NuttX

Which communication architecture are we using to connect are computers
to the drone: Peer2Peer or centralized? What about the remote control -
drone communication? \* Compute Board to Flight Controller: Uses a
Peer-to-Peer architecture for direct communication. \* Remote Control to
Drone: Utilizes a Centralized architecture, with the remote control as
the central hub communicating with the drone\'s flight controller.

True or False: For manual flight control, the remote control
communicates with the drone over wifi. \* False, transmitters and drones
connect via a specific radio frequency

In order to know where the drone is in the world, it needs some form of
positioning sensor/algorithms, otherwise it would be flying blind. What
are the different types of positioning sensors available? Which do you
think we are going to use during the class? \* Camera, LIDAR, etc.

True or False: during our indoor flights, we can use the GPS sensor to
estimate the drone\'s position in the world. \* False; walls, roofs, and
other obstacles lead to weak signals and cannot establish a reliable GPS
location.

Are optical flow algorithms responsible for mapping the environment? If
not, can you describe conceptually what optical flow does? Optical flow
algorithms track movements and can recognize objects moving rather than
creating a new object.

Which potential sensors on a Drone enables 3D visual mapping? CPotential
sensors on a drone for 3D visual mapping include Lidar, stereo cameras,
RGB-D cameras, and time-of-flight cameras, as they can capture depth
information to create precise 3D models of the environment.

How does the Compute Board communicate with the Flight Controller? The
Compute Board communicates with the Flight Controller via serial
interfaces like UART, I2C, SPI, or CAN bus, enabling the coordination
between high-level processing and low-level flight control.

What is PX4 and where is it running on the drone? PX4 is an open-source
flight control software stack that runs on the Flight Controller,
providing necessary algorithms and functionalities for stabilizing and
controlling the drone's flight.

Which of these best describes MAVLink: 1. an operating system used on
the drone, 2. a sensor on the drone, 3. a communication protocol on the
drone, 4. a programming language 3

If I want to write a new, complex computer vision algorithm for the
drone, should I add it to the Flight Controller firmware? If not, where
should I add it and why? If you want to write a new, complex computer
vision algorithm for the drone, you should add it to the Compute Board
or an onboard companion computer because these platforms have more
computational resources and are better suited for handling advanced
tasks, while keeping flight control stable and modular.
