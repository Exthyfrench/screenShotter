import time
import pyautogui

# Set the number of seconds between screenshots
interval = 5

# Set the filename prefix
filename_prefix = "screenshot"

# Set the filetype
filetype = "png"

# Set the counter for the filenames
counter = 1

# Take screenshots indefinitely
while True:
  # Take a screenshot
  image = pyautogui.screenshot()
  
  # Generate the filename
  filename = f"{filename_prefix}_{counter}.{filetype}"
  
  # Save the screenshot
  image.save(filename)
  
  # Increment the counter
  counter += 1
  
  # Sleep for the specified interval
  time.sleep(interval)
