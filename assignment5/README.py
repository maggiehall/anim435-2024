#README
# Export FBX files

#note for professor
I honestly don't know if I did this assignment correctly. I follwed generally what you have in the lecture. When I ran the file in gitbash it would print to the log file but not in git bash, not sure what I was doing wrong there. I also don't know exactly what I'm looking for when I'm reading the errors that are printed as it is seeminglyy printing infinitely.

## Overview
This tool reads an assets name, task name  and a username from environment variables. This information will be formatted into a filepath and export the asset as an fbx.

This script also includes logging to track the proccess. The logging functions include details about exporting the fbx, and errors and warnings about missing or incorrect enviornment variables.
## Prerequisites
To use this python code, the environment variable must be defined in GitBash.  

    Follow This Setup:  
    #export ASSET=insert_your_asset_name  
    #export TASK=insert_your_task_name  
    #export USERNAME=insert_your_user_name  

    Environment Variables Description:  
    ASSET: The name of the asset in Maya you want to export.  
    TASK: A descriptive name for the task (e.g., "modeling" or "texturing").  
    USERNAME: Your username or identifier (can use default) 

These variables will be used to construct the file path and name.
## Logging
The Script uses the python logging module to log information, warning and errors. The logs are printed in the terminal but you can also save a file. 
    - info messages: show the start and completion of the script
    - warning messages: show when any environment variables (listed above) are missing. 
    - Error messages: logs any errors with asset selection of file export.
## Usage
```python
- '--Environment Variables': Retrieves ASSET, TASK and USERNAME as environment variable
- '--Export Directory': Defines a hardcoded export directory path in pathExportDirectory
- '--File Path': constructs the full FBX file path using the format: TASK_USERNAME_ASSET.fbx
- '--Export Command': Selects the asset by name and exports it as an FBX file with the constructed path.

```
