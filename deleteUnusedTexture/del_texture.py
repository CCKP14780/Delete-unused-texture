import maya.cmds as cmds
from pprint import pprint

def get_file_node():
    Shader = cmds.ls(sl=True)
    print(Shader)
    for i in Shader:
        try:
            con = cmds.listConnections('%s.outColor' % i)
        except:
            continue
        names = cmds.listConnections(con, type="mesh")
        
        #! filter out for only geometry
        try:
            for each in names:  
                pass

        except:
            print(f'GARBAGE SHADER : {i}')
            cmds.delete(i)
            continue
get_file_node()
