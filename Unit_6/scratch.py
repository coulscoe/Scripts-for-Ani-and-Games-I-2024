# //creates back right wheel
# polyCylinder -radius 1 -height 1 -subdivisionsX 20 -subdivisionsY 1 -subdivisionsZ 1 -axis 0 1 0 -roundCap 0 -createUVs 3 -constructionHistory 1;
# rotate -relative -objectSpace -forceOrderXYZ 90 0 0 ;
# move -relative 2.5 0 0 ;
# move -r 0 1 0 ;
# move -r 0 0 2;
# //creates back left wheel
# polyCylinder -radius 1 -height 1 -subdivisionsX 20 -subdivisionsY 1 -subdivisionsZ 1 -axis 0 1 0 -roundCap 0 -createUVs 3 -constructionHistory 1;
# rotate -relative -objectSpace -forceOrderXYZ 90 0 0 ;
# move -relative 2.5 0 0 ;
# move -relative 0 1 0 ;
# move -relative 0 0 -2;
#
# //creates top of truck
# polyCube -width 3 -height 2 -depth 4 -subdivisionsX 1 -subdivisionsY 1 -subdivisionsZ 1 -axis 0 1 0 -createUVs 4 -constructionHistory 1;
# move -relative 0 4 0 ;
# move -relative -1.5 0 0 ;
# select -replace pCube2.e[6] ;
# move -relative 1.612513 0 0 ;
#
# //creates truck bed
# select -replace pCube1.f[25:28] pCube1.f[35:38] pCube1.f[45:48] pCube1.f[55:58] pCube1.f[65:68] pCube1.f[75:78] pCube1.f[85:88] pCube1.f[95:98] ;
# polyExtrudeFacet -constructionHistory 1 -keepFacesTogether 1 -pvx 1.599999845 -pvy 3.5 -pvz 5.960464478e-08 -divisions 1 -twist 0 -taper 1 -off 0 -thickness 0 -smoothingAngle 30 pCube1.f[25:28] pCube1.f[35:38] pCube1.f[45:48] pCube1.f[55:58] pCube1.f[65:68] pCube1.f[75:78] pCube1.f[85:88] pCube1.f[95:98];
# setAttr "polyExtrudeFace1.localTranslateZ" -1.9;
#
# //creates left headlight
# polyCylinder -radius 1 -height 1 -subdivisionsX 20 -subdivisionsY 1 -subdivisionsZ 1 -axis 0 1 0 -roundCap 0 -createUVs 3 -constructionHistory 1;
# rotate -relative -objectSpace -forceOrderXYZ 0 0 90 ;
# move -relative 0 2 0 ;
# scale -relative 0.5 0.5 0.5;
# move -relative -3.9 0 0 ;
# move -relative 0 0 -1.2 ;
#
# //creates right headlight
# polyCylinder -radius 1 -height 1 -subdivisionsX 20 -subdivisionsY 1 -subdivisionsZ 1 -axis 0 1 0 -roundCap 0 -createUVs 3 -constructionHistory 1;
# rotate -relative -objectSpace -forceOrderXYZ 0 0 90 ;
# move -relative 0 2 0 ;
# scale -relative 0.5 0.5 0.5;
# move -relative -3.9 0 0 ;
# move -relative 0 0 1.2 ;
import maya.cmds as cmds
from maya.app.renderSetup.model.plug import relatives
#created truck body
cmds.polyCube( width=8, height=2, depth=4, subdivisionsX=10, subdivisionsY=1, subdivisionsZ=10, axis =[0,1,0], createUVs=4, constructionHistory=1)
cmds.move(0,2,0, relative=True)
# creates wheels
# creates front right wheel
cmds.polyCylinder (radius=1, height=1, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=1,axis=[0,1,0],roundCap=0,createUVs=3,constructionHistory=1)
cmds.rotate(90,0,0, relative=True,objectSpace=True, forceOrderXYZ=True)
cmds.move(-3,1,2,relative=True)
#creates front left wheel
cmds.polyCylinder(radius=1,height=1,subdivisionsX=20,subdivisionsY=1,subdivisionsZ=1,axis= [0,1,0],roundCap=0,createUVs=3,constructionHistory=True)
cmds.rotate( 90,0,0,relative=True,objectSpace=True,forceOrderXYZ=True)
cmds.move(-3,1,-2,relative=True)
# creates back right wheel
cmds.polyCylinder(radius=1,height=1,subdivisionsX=20,subdivisionsY=1,subdivisionsZ=1,axis=[0,1,0],roundCap=0, createUVs=3,constructionHistory=True)
cmds.rotate(90, 0,0,relative=True,objectSpace=True,forceOrderXYZ=True)
cmds.move(2.5,1,2,relative=True)
# creates back left wheel
cmds.polyCylinder(radius=1,height=1,subdivisionsX=20,subdivisionsY=1,subdivisionsZ=1,axis=[0,1,0], roundCap=0,createUVs=3, constructionHistory=True)
cmds.rotate( 90,0,0,relative=True,objectSpace=True, forceOrderXYZ=True)
cmds.move(2.5,1,-2,relative=True)
# creates top of truck
cmds.polyCube(width=3,height=2,depth=4,subdivisionsX=1,subdivisionsY=1,subdivisionsZ=1,axis=[0,1,0],createUVs=4,constructionHistory=True)
cmds.move(-1.5,4,0, relative=True)
cmds.select(pCube2.e[6], replace=True)
cmds.move(1.612513,0,0, relative=True)
