import argparse
import maya.standalone
maya.standalone.initialize()
import maya.cmds

#testing sumbission
#Created entire new directory

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--radius', help =)
maya.cmds.polySphere()
maya.cmds.file(rename="C:\Users\maggi\OneDrive - Drexel University\Year3\fallWinter\techDirecting\week3\anim435-2024\standalone_example\mewsphere.mb")