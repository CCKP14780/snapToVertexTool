import maya.cmds as cmds
import mtoa.utils as mutils

def createBulb(nam = 'bulb',r = 1):
    sel = cmds.ls(sl=True)
    vtx_count = cmds.polyEvaluate(sel,v=True)

    for i in range(vtx_count):
        
        obj = cmds.polySphere(name=f'{nam}_{vtx_count}',radius = r)[0]
        vtxID = f'{sel[0]}.vtx[{i}]'
        pos = cmds.xform(vtxID,q=True,t=True,ws=True)
        print(vtxID,pos)
        
        cmds.xform(obj,t = pos,ws = True)
               
createBulb()

#cmds.warning(<'string'>)