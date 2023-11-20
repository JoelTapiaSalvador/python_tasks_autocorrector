# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 03:09:20 2023

@author: JoelT
"""
import importlib


###############################################################################
#        WRITE HERE THE FILE NAME OF YOUR SCRIPT AND EXECUTE THE FILE         #
FILE_NAME_YOUR_SCRIPT = "test_submission.py"
###############################################################################


LIST_SEPARATORS = ["="]
LIST_COMMENTATORS = [">>>"]
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
    global SPEC
    global MODULE
    SPEC = importlib.util.spec_from_file_location(module_name, file_path)
    MODULE = importlib.util.module_from_spec(SPEC)


def test_1():
    """
    Test number 1.

    Returns
    -------
    None.

    """
    print(LIST_SEPARATORS[0] * WIDTH + " Test 1 " + LIST_SEPARATORS[0] * WIDTH)
    SPEC.loader.exec_module(MODULE)


def test_2():
    """
    Test number 2.

    Returns
    -------
    None.

    """
    print(LIST_SEPARATORS[0] * WIDTH + " Test 2 " + LIST_SEPARATORS[0] * WIDTH)
    print(LIST_COMMENTATORS[0] + " Tested")


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
    module_from_file("Autocorrection", file_path_module)
    main()


def main():
    """
    Executes all the test functions in order.

    Returns
    -------
    None.

    """
    test_1()
    test_2()


if __name__ == "__main__":
    module_from_file("Your script", FILE_NAME_YOUR_SCRIPT)
    main()
