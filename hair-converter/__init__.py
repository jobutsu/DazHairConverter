bl_info = {
    "name": "Daz Mesh Hair Converter",
    "author": "Cinus - Modified by Jobutsu",
    "version": (2,1,1),
    "blender": (3,2,1),
    "description": "Convert mesh hair to particle hair",
    "category": "Object"}

import sys
import importlib

modulesNames = ['hair']
 
modulesFullNames = {}
for currentModuleName in modulesNames:
    if 'DEBUG_MODE' in sys.argv:
        modulesFullNames[currentModuleName] = ('{}'.format(currentModuleName))
    else:
        modulesFullNames[currentModuleName] = ('{}.{}'.format(__name__, currentModuleName))
 
for currentModuleFullName in modulesFullNames.values():
    if currentModuleFullName in sys.modules:
        importlib.reload(sys.modules[currentModuleFullName])
    else:
        globals()[currentModuleFullName] = importlib.import_module(currentModuleFullName)
        setattr(globals()[currentModuleFullName], 'modulesNames', modulesFullNames)
 
def register():
    for currentModuleName in modulesFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'initialize'):
                sys.modules[currentModuleName].initialize()
 
def unregister():
    for currentModuleName in modulesFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'uninitialize'):
                sys.modules[currentModuleName].uninitialize()
 
if __name__ == "__main__":
    register()
