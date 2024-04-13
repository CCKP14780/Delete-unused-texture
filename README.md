#paste the deleteUnusedTexture folder to C:\Users\User\OneDrive\Documents\maya\<version>\scripts 

#paste this code in Maya script editor
import maya.cmds as cmds
import importlib
import deleteUnusedTexture.del_texture as tx
importlib.reload(tx)

#NOTE: this code fragment can also be found in the README.txt from the deleteUnusedTexture folder.
