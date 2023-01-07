# screenShotter
This script uses the PyAutoGUI library to take screenshots, and the time library to pause the script for a specified interval between screenshots.
It generates a filename using the prefix, counter, and filetype, and saves the screenshot to that file.

To use this script, save it to a file (e.g. screenshotter.py) and run it using Python:

-- python screenshotter.py


The script will run indefinitely, taking a screenshot every 5 seconds (or whatever interval you specify) and saving it to a file. 
You can stop the script by pressing CTRL + C.

If you want to run the script in the background, you can use a tool like nohup or screen to run it in a detached session.

For example, you can use the following command to run the script using nohup:
-- nohup python screenshotter.py &


This will run the script in the background and allow you to close the terminal or log out of the system without stopping the script. 
The nohup command will also prevent the script from being terminated when the terminal is closed.
