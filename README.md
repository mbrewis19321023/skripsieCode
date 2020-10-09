# skripsieCode
This is all the python code that you used for skripsie 

Versions will only be properly named from 2.1. Version 2.1 is the introduction of the driver folder finder functionality.
Version 1.x was the creation of the dataFrame and sanitation.

Version 1.5: renamed the path.py to mypath.py to avoid errors when using os.path 

Version 1.5.1: renamed the path.py to mypath.py to avoid errors when using os.path. Fixed README.md

Version 2.1: Began addiding functionality for going into folders and going out of them. Tried to do so using recurring function calls. Perhaps a bad idea? Sort of working. Saved as driverFind. Next time look for a simpler way to do this. Perhaps save a place in the file tree somehow?

Version 2.2: Can identify the Driver folders for a number of students in stdRepos folder. Adds the path of these Driver folders to the data frame for specific students. Pretty robust as it can go pretty far into folders. Wrote this using a recurring function call. For the next version, make sure it works on a big repository and export the frame.

Version 2.3: Changed the functionality of the second program to identify the Core folder instead. Made some of the terminal messages better. Also renamed to programs to Step_1 and Step_2. Made changes to how the dataframe is imported in the second program; it now goes to the data folder and imports the dataframe to csv made by the first program. Great job. For the next verion identify the pins and save each pinout to a csv perhaps per student hash.