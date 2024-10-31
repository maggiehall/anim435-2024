#README
# Export FBX files
## Overview
This tool reads an assets name, task name  and a username from environment variables. This information will be formatted into a filepath and exports the asset as an fbx.

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

## Usage
```python
- '--Environment Variables': Retrieves ASSET, TASK and USERNAME as environment variable
- '--Export Directory': Defines a hardcoded export directory path in pathExportDirectory
- '--File Path': constructs the full FBX file path using the format: TASK_USERNAME_ASSET.fbx
- '--Export Command': Selects the asset by name and exports it as an FBX file with the constructed path.

```