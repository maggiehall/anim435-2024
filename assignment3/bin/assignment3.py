import argparse
import maya.standalone
maya.standalone.initialize()
import maya.cmds as cmds

# function for making lambert material
def createMaterial(color):
    materialName = cmds.shadingNode('lambert', asShader=True)
    cmds.setAttr(materialName + '.color', color[0], color[1], color[2], type='double3')
    return materialName

#fcn to create cube with material
def createCube(color):
    myCube = cmds.polyCube(width=5, height=5, depth=5)[0]
    material = createMaterial(color)
    cmds.select(myCube)
    cmds.hyperShade(material, assign=True)
    return myCube

#fcn to create cphere with material
def createSphere(color):
    mySphere = cmds.polySphere(radius=5)[0]
    material = createMaterial(color)
    cmds.select(mySphere)
    cmds.hyperShade(assign=material)
    return mySphere

# Setting up argparse for command line options
#creating parser object
parser = argparse.ArgumentParser(description="Create 3D shapes with materials in MayaPy.")
parser.add_argument('--shape', choices=['cube', 'sphere'], required=True, help="Shape to create: cube or sphere")
parser.add_argument('--color', choices=['red', 'green', 'blue', 'white'], default='white', help="Color of the shape's material")
parser.add_argument('--output', required=True, help="Path to save the Maya file (.mb)")

args = parser.parse_args()
print(args.color)
# defining the colors
if args.color == 'red':
    color = (1.0, 0.0, 0.0)
elif args.color == 'green':
    color = (0.0, 1.0, 0.0)
elif args.color == 'blue':
    color = (0.0, 0.0, 1.0)
else:
    color = (1.0, 1.0, 1.0)  # Default to white
print(color)

# Creating the shape
if args.shape == 'cube':
    print("Creating a cube...")
    createCube(color)
elif args.shape == 'sphere':
    print("Creating a sphere...")
    createSphere(color)


# Save the Maya file

maya.cmds.file(rename=args.output)
maya.cmds.file(save=True)
print(f"Saved file to {args.output}")

'''
anytime I try to use gitBash  to create a new
maya file, or do anything in maya with vs code,
I getan error for no such file or directory
this is the line I was using:

mayapy "/c/Users/maggi/OneDrive - Drexel University/Year3/fallWinter/techDirecting/week3/anim435-2024/assignment3_v002/anim435-2024/assignment3/make-sphere.py"

'''
