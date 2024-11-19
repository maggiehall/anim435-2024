# assignment 6: Metadata
# add metadata export using the Python json module to a previous assignment
# using assignment 5
    #Export FBX files using environment variables
    #include logging

#for this code to work, you MUST use the provided
# environment variables. use the below code in 
# GitBash to define these variables

    #export ASSET=insert_your_asset_name
    #export TASK=insert_your_task_name
    #export USERNAME=insert_your_user_name

#code for maya
import os
import maya.cmds as cmds
import json
import logging
logger = logging.getLogger(__name__)

# this syntax is from class
FORMAT = "[%(asctime)s][%(filename)s][%(levelname)s]%(msg)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)

#access and define enviornment variables from git bash
assetName = os.getenv("ASSET")
task = os.getenv("TASK")
username = os.getenv("USERNAME")

logger.info("Starting FBX export script...")

#use logging to check if the env variables are set
if not assetName:
    logger.error("Environment variable ASSET is not set.")
if not task:
    logger.warning("Environment variable TASK is not set. Defaulting to 'unknown_task'.")
    task = "unknown_task"
if not username:
    logger.warning("Environment variable USERNAME is not set. Defaulting to 'unknown_user'.")
    username = "unknown_user"

#define file path for fbx asset folder
pathExportDirectory = r"C:\Users\maggi\OneDrive - Drexel University\Year3\fallWinter\techDirecting\anim435-2024-mh3775\midterm\maya\assets"

#add environment variables to create the structurred fbx path
fileName = f"{task}_{username}_{assetName}.fbx"
filepath = os.path.join(pathExportDirectory, fileName)

#metadata dictionary
data = {
    "assetName": assetName,
    "task": task,
    "username": username,
    "exportpath": filepath,
    "exportStatus": "failed", #failed for default, will update if successful
}

#use logging to see if asset is properly selected and exported
try:
    # Attempt to select the asset
    if cmds.objExists(assetName):
        cmds.select(assetName)
        logger.info(f"Asset '{assetName}' selected for export.")
    else:
        logger.error(f"Asset '{assetName}' does not exist in the scene. Export failed.")

    # Attempt to export the FBX file
    cmds.file(filepath, force=True, options="v=0;", typ="FBX export", pr=True, es=True)
    logger.info(f"Successfully exported asset to '{filepath}'")

    #update metadata on sucess
    data["exportStatus"] = "success"

except Exception as e:
    logger.error(f"Failed to export FBX: {e}")

#write metadata to JSON file
metadata_file = os.path.join(pathExportDirectory, "metadata.json")
try:
    with open(metadata_file, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f"Metadata successfully written to '{metadata_file}'")
except Exception as e:
    logger.error(f"Failed to write metadata: {e}")
logger.info("Finished FBX export script.")