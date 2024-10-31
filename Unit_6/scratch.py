import maya.cmds as cmds
object=[]
# created truck body
object=cmds.polyCube( width=8, height=2, depth=4, subdivisionsX=10, subdivisionsY=1, subdivisionsZ=10, axis =[0,1,0], createUVs=4, constructionHistory=1)
cmds.move(0, 2, 0, object)
# creates wheels
# creates front right wheel
object=cmds.polyCylinder(radius=1,height=1,subdivisionsX=20,subdivisionsY=1,subdivisionsZ=1,axis= [0,1,0],roundCap=0,createUVs=3,constructionHistory=True)
cmds.rotate(90, 0, 0, object,objectSpace=True, forceOrderXYZ=True)
cmds.move(-3, 1, 2, object)
# creates front left wheel
object=cmds.polyCylinder(radius=1,height=1,subdivisionsX=20,subdivisionsY=1,subdivisionsZ=1,axis= [0,1,0],roundCap=0,createUVs=3,constructionHistory=True)
cmds.rotate( 90,0,0,object,objectSpace=True,forceOrderXYZ=True)
cmds.move(-3,1,-2,object)
# creates back right wheel
object=cmds.polyCylinder(radius=1,height=1,subdivisionsX=20,subdivisionsY=1,subdivisionsZ=1,axis=[0,1,0],roundCap=0, createUVs=3,constructionHistory=True)
cmds.rotate(90, 0,0,object,objectSpace=True,forceOrderXYZ=True)
cmds.move(2.5,1,2,object)
# creates back left wheel
object=cmds.polyCylinder(radius=1,height=1,subdivisionsX=20,subdivisionsY=1,subdivisionsZ=1,axis=[0,1,0], roundCap=0,createUVs=3, constructionHistory=True)
cmds.rotate( 90,0,0,object,objectSpace=True, forceOrderXYZ=True)
cmds.move(2.5,1,-2,object)
# creates top of truck
object=cmds.polyCube(width=3,height=2,depth=4,subdivisionsX=1, subdivisionsY=1,subdivisionsZ=1,axis=[0,1,0], createUVs=4, constructionHistory=True)
cmds.move(-1.5,4,0, relative=True)
cmds.select('pCube6.e[6]')
cmds.move(1.612513,0,0,relative=True)
# creates left headlight
object=cmds.polyCylinder(radius=1,height=1,subdivisionsX=20,subdivisionsY=1,subdivisionsZ=1,axis=[0,1,0],roundCap=0,createUVs=3,constructionHistory=True)
cmds.rotate(0,0,90,object,relative=True,objectSpace=True, forceOrderXYZ=True)
cmds.move( -3.9,2,-1.2,object,relative=True)
cmds.scale( 0.5,0.5,0.5,object,relative=True)
#creates right headlight
object=cmds.polyCylinder(radius=1,height=1,subdivisionsX=20,subdivisionsY=1,subdivisionsZ=1,axis=[0,1,0],roundCap=0,createUVs=3,constructionHistory=True)
cmds.rotate(0,0,90,object,relative=True,objectSpace=True, forceOrderXYZ=True)
cmds.move( -3.9,2,1.2,object,relative=True)
cmds.scale( 0.5,0.5,0.5,object,relative=True)
