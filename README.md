# Python 3 Tk based Desktop GUI App template

### What is this? 

In terms of an MVC design pattern,
The framework includes the skeleton for the "model" and state permanence as well as supporting data structures for this. 
It also includes wrappers to simplify the creation of the UI, or the "view", and has common control flows implemented (page navigation)
It also includes the logical structure and file structure to support the implementation of the underlying controller code in /lib/app

### Origins

This was forked from a Python software engineering group coursework I made in my Engineering Foundation Year.
99% of the code is mine as I was the only one who could actually code amongst the engineers.
The source code for the [rotational-dynamics-python](https://github.com/yaq1n0/rotational-dynamics-python) coursework
can be found here.

### Seeing Potential

I saw the potential in repurposing the GUI elements and codebase for the coursework into a template/framework that I
could use in the future.
I eventually want to make it such that I can quickly implement backend functionality separately to the front-end in a
way that is similar to and will be simple to port over to a web-app type deployment with flask.

## Documentation

### Directory Structure
- main.py : program entry point
- README.md : you are here
- /lib : library for everything. 

- lib/app : your core back-end app code goes here (I suggest using static atomic functions that can be called from the rest of the code)

- lib/components : you core front-end app code goes here. Each "Page" of the app has its own class file here. Object instance is used and passed around (Singleton design pattern). 

- /lib/resources/config : configuration JSONs go here (you can encourage end user editing of these files, but I suggest using the a preference page for this, so that you can sanitize user configurations. )
- /lib/resources/images: program image resources go here

- /lib/core : contains functions responsible for handling core desktop-app-template functionality (preferences, theming etc. )

- /lib/ui : contains all UI elements that can be used (import UI elements from here)
- /lib/ui/tk-utils : contains helper functions that simplify repetitive tk actions. 
- /lib/ui/tk-widgets : contains the Class files for the App versions of the tkinter base widgets
- /lib/ui/compound-widgets : contains the Class files for custom compound widgets made from tk-widgets. 
- /lib/ui/app-widgets : here is where you would put your own custom widgets for your app, if you need them

### imports best practices to prevent circular dependencies
- only import as needed, avoid wildcard imports where possible
- nothing should be imported into /lib/core
- import ui components straight from /lib/ui. Internal import routing should be handled by /lib/ui/__init__.py

### How to use (developer)

- Use the included DemoPage.py and TemplatePage.py as a start point for creating the UI using the App's built in widgets
- To contribute new AppWidgets, use the App<name> convention to prevent conflicts with Tk's default widgets.
  also try to use polymorphic inheritance from the original Tk widgets.
- To contribute new components, use the <name>Page convention
- To contribute new functions, use generate_<function> and/or common sense :P

### How to use (end-user)

- The preferences page should have useful options such as setting the resolution of the program window, and enabling
  certain settings.

## Features to be added

- DemoPage with most of the widgets implemented for demo purposes.
- For some reason the program_restart function only works once, I'm assuming it's some kinda pid issue.
  Long term solution might be to remove the need for having to restart the program at all. 