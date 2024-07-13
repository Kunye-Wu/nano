Qset 1:
**List all rosnodes that exist after running the publisher:**
minimal\_publisher, minimal\_subscriber
**List all rostopics that are being present after running the publisher**
topic
**What command do I run to see what is being published to a topic?**
ros2 topic echo /topic
**What would I change in the publisher to make it publish messages more frequently?**
You would change the timer\_period variable to change the time in between every message publish
**In terminal I run the python script for the subscriber and see information being printed. Does this mean it is publishing to a topic?**
No, it means that the subscriber is recieving messages from the publisher
**What is the main benefit of a composed node? How might this help in drone autonomy applications?**
Composed nodes simplify code reuse, and are also more memory efficient and perform better. This can be important for quickly processing autonomous tasks, which is important especially for a flying object

Qset 2:
**What is needed to be added to the launch file?**
A Python, XML, or YAML file with node information needs to be added to the launch file
**With rqt_graph open, use the button in upper right corner to save an image of the graph and include it in this report. Which components in the graph indicates rosnodes and which indicate rostopics?**
Included as attachment in team\_submissions\_md. The circled ellipses indicate nodes and the boxed text indicate topics
**Why do we need to run the command when and why do we need to source a bash file?**
Sourcing the bash file is for setting up the workspace, and you need to run the command every time you want to do so, usually every time using ROS.
**Were there any steps that didn't work or were particularly confusing? How did you work around them?**
Not too many, this one was much more straightforward than the last exercise.
