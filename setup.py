
    # What does this do? 

    # Andrew: This specifies licenses, author, version, etc.. Also the find_packages command goes through the root folder of directory and finds packages and dependencies associated with it!

    # setup command:
    # "pip install -e ."

    # create build package, command:
    # "python setup.py sdist bdist_wheel"


from setuptools import setup, find_packages

setup (
    name = "src",
    version = "0.0.1",
    description="computer vision version 1 test",
    author="aschonn",
    packages=find_packages(),
    license="MIT")