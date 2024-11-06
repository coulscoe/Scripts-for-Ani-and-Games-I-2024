import maya.cmds as cmds
def group_tool():
    sels= cmds.ls(selection=True)
    objTest=cmds.group(sels, name="objTest")
    print(objTest)
group_tool()