import maya.cmds as cmds
def group_tool():
    sels= cmds.ls(selection=True)
    for sel in sels:
        position=cmds.xform(sel, q=True, ws=True, t=True)
        rotation=cmds.xform(sel, q=True, ws=True, ro=True)
        obj_group = cmds.group(sel)
group_tool()