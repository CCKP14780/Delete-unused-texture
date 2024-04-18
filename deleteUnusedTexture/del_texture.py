import maya.cmds as cmds

def get_file_node():
    Shader = cmds.ls(sl=True)
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
            if i == 'lambert1' or i == 'particleCloud1' or i == 'standardSurface1':
                pass
            
            else:
                print(f'GARBAGE SHADER : {i}')
                try:
                    cmds.delete(i)
                except:
                    print(f'Default or Reference Shader {i}. Deletion withdrawn')
get_file_node()
