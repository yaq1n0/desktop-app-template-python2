# This file contains the schema for the config files
### this file should help you understand how the app handles its configuraton
The current app state information is stored as /lib/resources/config/user_config.json. 

This json is read and wrote to using atomic python functions that handle error checking. 

If you want to make changes to the files governing app configuration, adhere to the following best practices: 
- always keep track of modifications to the schema in this document, so that you can ensure consistency across the app
- validate your reads before you start using the data from it
- validate your writes before you write to file

### atomic functions
`read_user_config : read from user_config.json`
`write_user_config : write to user_config.json`
`reload_default_config : write default_config to user_config.json`

### config.json example
```
{
    "font": "System",
    "font_size": 12,
    "enable_tooltips": "True",
    "enable_developer": "False",
    "theme_color_1": "#101010",
    "theme_color_2": "#FFFFFF",
    "theme_color_3": "#0080D0"
}
```

### everything in the config can be one of the following: 
- a pure string like font, 
- a number like font_size 
- a boolean stored as a string 
- a hexadecimal stored as a string 
