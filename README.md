# Python 3 Tk based Desktop GUI App template

### Origins

This was forked from a Python software engineering group coursework I made in my Engineering Foundation Year.
99% of the code is mine as I was the only one who could actually code amongst the engineers.
The source code for the [rotational-dynamics-python](https://github.com/yaq1n0/rotational-dynamics-python) coursework
can be found here.

### Seeing Potential

I saw the potential in repurposing the GUI elements and codebase for the coursework into a template/framework that I
could use in the future.
I eventually want to make it such that I can quickly implement backend functionality seperately to the front-end in a
way that is similar to and will be simple to port over to a web-app type deployment with flask. 

## Documentation 
### Directory Structure
 - run.py : program entry point
 - readme.md : you are here
 - resources : where to find and store media files (non-code objects)
 - lib : main library directory, all the code goes here
 - lib/components : this directory contains all the individual pages (components) of the app
 - lib/functions : this directory contains helpful (in my opinion) functions for the app
 - lib/widgets : this directory contains widgets that follow the app's design style 
using the App<name> naming convention prevents conflict with the similarly named Tk default widgets
 - lib/app_root.py : this file contains the global app variables (user_preferences, fonts, etc), 
and functions for reading and writing these to the JSON that is used for disk permanence  

### How to use (developer)
 - Use the included DemoPage.py and TemplatePage.py as a start point for creating the UI using the App's built in widgets
 - To contribute new AppWidgets, use the App<name> convention to prevent conflicts with Tk's default widgets. 
also try to use polymorphic inheritance from the original Tk widgets.
 - To contribute new components, use the <name>Page convention 
 - To contribute new functions, use generate_<function> and/or common sense :P

### How to use (end-user)
 - The preferences page should have useful options such as setting the resolution of the program window, and enabling certain settings. 

## Features to be added 
 - Fully responsive UI! no longer needing to manually set the viewport resolution. 
This should be possible but would require massive refactoring of the codebase. 