#README
# Export FBX files
## overview
this tool reads an assets name, task name  and a username from environment variables. This information will be formatted into a filepath and exports the asset as an fbx.

## Prerequisites
To use this python code, the environment variable must be defined in GitBash.
follow this setup:
    #export ASSET=insert_your_asset_name
    #export TASK=insert_your_task_name
    #export USERNAME=insert_your_user_name
    
I used this:
    export ASSET=cubeShape
    export TASK=model
    export USERNAME=maggie

These variable will be used to contruct the file path and name

## Usage
```
1. Environment Variables: Retrieves ASSET, TASK and USERNAME as environment variable
2. Export Directory: Defines a hardcoded export directory path in pathExportDirectory
3. File Path: constructs the full FBX file path using the format: TASK_USERNAME_ASSET.fbx
4. Export Command: Selects the asset by name and exports it as an FBX file with the constructed path.

```