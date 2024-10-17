import argparse
import maya.standalone
maya.standalone.initialize()
import maya.cmds

#creating parser object
parser = argparse.ArgumentParser()
parser.add_argument('r', '--radius', default=1)

args = parser.parse_args()

print("creating a sphere")

maya.cmds.polySphere(radius=args.radius)
maya.cmds.file(rename=r"C:\Users\maggi\OneDrive - Drexel University\Year3\fallWinter\techDirecting\week3\anim435-2024\standalone_example\newsphere.mb")
maya.cmds.file(save=True)

print(f"Created a sphere of size {args.radius}.")


'''
anytime I try to use gitBash  to create a new
maya file, or do anything in maya with vs code,
I getan error for no such file or directory
this is the line I was using:

mayapy "/c/Users/maggi/OneDrive - Drexel University/Year3/fallWinter/techDirecting/week3/anim435-2024/assignment3_v002/anim435-2024/assignment3/make-sphere.py"

'''
