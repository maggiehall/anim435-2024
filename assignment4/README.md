# project Directory Setup tool
## Overview
this scrips will be used in maya. It uses environment variables set in a Bash shell to create the Maya ProjectDirectory

## Environment Variables
- `SHOT`: Represents the current shot.
- `PROJECT_DIR`: The main directory for the Maya project.
- `TASK`: The specific task associated with the project.

## usage
- uses the `PROJECT_DIR` environment variable to set a maya proj directory
- listed below are th efolders created in the project directory:
    - `scenes`
     - `sourceimages`
     - `images`
     - `clips`
     - `sound`
     - `python` (for scripts)
     - `cache`
     - `autosave`
- before making he folder there is verification to make sure the folder does not already exist
