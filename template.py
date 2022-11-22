import os


'''
    Source files directory template
'''

dirs = [
    # adds data to path (makes life easier)
    os.path.join("data", "raw"),
    os.path.join("data","processed"),

    #models
    "notebooks"

    #saved models
    "saved_models"

    #utility functions for preprocessing and such
    "src"
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass


files = [

    # runs commands for preprocessing data before github commit
    "dvc.yaml",
    # specific paramaters for models (manually changed)
    "params.yaml",
    # github ignore files file
    ".gitignore",
    os.path.join("src","__init__.py")
]

for file_ in files:
    with open(file_, "w") as f:
        pass
