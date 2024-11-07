import maya.cmds as cmds
def group_tool():
    sels= cmds.ls(selection=True)
    for sel in sels:
        position=cmds.xform(sel, q=True, ws=True, t=True)
        rotation=cmds.xform(sel, q=True, ws=True, ro=True)
        obj_group = cmds.group(sel, empty=True, name=f'{sel}_Grp')
        cmds.xform(obj_group, ws=True, t=position)
        cmds.xform(obj_group, ws=True, ro=rotation)
        parent_obj=cmds.parent(sel, obj_group)
group_tool()