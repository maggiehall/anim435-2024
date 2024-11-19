#README
# Export FBX files

## Overview
This tool reads an assets name, task name  and a username from environment variables. This information will be formatted into a filepath and export the asset as an fbx.

This script includes logging to track the proccess. The logging functions include details about exporting the fbx, and errors and warnings about missing or incorrect enviornment variables.

This scripts includes a dictionary that holds metadata. This metadata will be exported to a json file. 
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
## Metadata
The script uses  dictionary titled "data" to contain information of the asset name, task, username, export path and export status. The export status defaults to 'failed' but will update if the export is succesful. This data is exported to a json file.
## Usage
```python
- '--Environment Variables': Retrieves ASSET, TASK and USERNAME as environment variable
- '--Export Directory': Defines a hardcoded export directory path in pathExportDirectory
- '--File Path': constructs the full FBX file path using the format: TASK_USERNAME_ASSET.fbx
- '--Export Command': Selects the asset by name and exports it as an FBX file with the constructed path.

```


#README
tags store arbritary data, there is also info in a structure that gets put into a file on disk

json notes:
- 'dump' writes to a file
- 'load' reads in from a file
- all im doing is taking a dictionary from pythin and writing it to a file

min 28 for dictioary creation in gitbash