# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 03:09:20 2023

@author: JoelT
"""
import importlib


###############################################################################
#        WRITE HERE THE FILE PATH TO YOUR SCRIPT AND EXECUTE THE FILE         #
FILE_PATH_TO_YOUR_SCRIPT = "submission.py"
###############################################################################


SEPARATOR = "-"
WIDTH = 41


def module_from_file(module_name: str, file_path: str):
    """
    Imports a module from any given path, usefull when a module is not in the
    same directory of the main program.

    Parameters
    ----------
    module_name : string
        Name showed in value of variable explorer, can be anything, doesn't
        need to mach with variable name or file name.
    file_path : string
        Relative path from main program to the module mean to be imported,
        including name of the file with the module to be imported or absolute
        path to the module mean to be imported, including name of the file with
        the module to be imported.

    Returns
    -------
    None.

    """
    global spec
    global module
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)


def test_1():
    print(SEPARATOR * WIDTH + " Test 1 " + SEPARATOR * WIDTH)
    spec.loader.exec_module(module)


def autocorrector(file_path_module: str):
    """
    Function for the autocorrector to call when evaluaing scripts.

    Parameters
    ----------
    file_path_module : str
        File path of the script to be tested.

    Returns
    -------
    None.

    """
    module_from_file("Module from autocorrection", file_path_module)
    main()


def main():
    """


    Returns
    -------
    None.

    """
    test_1()


if __name__ == "__main__":
    module_from_file("Module from your script", FILE_PATH_TO_YOUR_SCRIPT)
    main()
