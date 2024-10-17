import argparse
import maya.standalone
maya.standalone.initialize()
import maya.cmds

#testing sumbission
#Created entire new directory

maya.cmds.polySphere()
maya.cmds.file(rename=r"C:\Users\maggi\OneDrive - Drexel University\Year3\fallWinter\techDirecting\week3\anim435-2024\standalone_example\newsphere.mb")
maya.cmds.file(save=True)

