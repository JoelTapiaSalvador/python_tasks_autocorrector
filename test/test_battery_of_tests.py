# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 03:09:20 2023

@author: JoelT
"""
import json
import importlib
import traceback


###############################################################################
#                   WRITE HERE THE FILE NAME OF YOUR SCRIPT                   #
#                           AND EXECUTE THIS SCRIPT                           #
FILE_NAME_OF_YOUR_SCRIPT = "test_submission.py"
###############################################################################

###############################################################################
#                                   OPTIONS                                   #
LIST_COMMENTATORS = [">>>"]
LIST_SEPARATORS = ["="]
WIDTH = 41
###############################################################################


def module_from_file(module_name: str, file_path: str):
    """
    Imports a module from any given path.

    Parameters
    ----------
    module_name : String
        Name showed in value of variable explorer, can be anything, doesn't
        need to mach with variable name or file name.
    file_path : String
        Relative path from main program to the module mean to be imported,
        including name of the file with the module to be imported or absolute
        path to the module mean to be imported, including name of the file with
        the module to be imported.

    Returns
    -------
    (ModuleSpec, Module)
        Tuple of objects obtained from calling
        "importlib.util.spec_from_file_location()" and
        "importlib.util.module_from_spec()" respectively.

    """
    __spec = importlib.util.spec_from_file_location(module_name, file_path)
    __module = importlib.util.module_from_spec(__spec)

    return __spec, __module


def test_1(internal_spec, internal_module):
    """
    Test number 1.

    Parameters
    ----------
    internal_spec : ModuleSpec
        Object obtained from calling
        "importlib.util.spec_from_file_location()".
    internal_module : Module
        Object obtained from calling "importlib.util.module_from_spec()".

    Returns
    -------
    None.

    """
    print(LIST_SEPARATORS[0] * WIDTH + " Test 1 " + LIST_SEPARATORS[0] * WIDTH)

    internal_spec.loader.exec_module(internal_module)


def test_2(internal_spec, internal_module):
    """
    Test number 2.

    Parameters
    ----------
    internal_spec : ModuleSpec
        Object obtained from calling
        "importlib.util.spec_from_file_location()".
    internal_module : Module
        Object obtained from calling "importlib.util.module_from_spec()".

    Returns
    -------
    None.

    """
    print(LIST_SEPARATORS[0] * WIDTH + " Test 2 " + LIST_SEPARATORS[0] * WIDTH)

    if internal_module is None or internal_spec is None:
        return
    print(LIST_COMMENTATORS[0] + " Tested")


def test_3(internal_spec, internal_module):
    """
    Test number 3.

    Parameters
    ----------
    internal_spec : ModuleSpec
        Object obtained from calling
        "importlib.util.spec_from_file_location()".
    internal_module : Module
        Object obtained from calling "importlib.util.module_from_spec()".

    Returns
    -------
    None.

    """
    print(LIST_SEPARATORS[0] * WIDTH + " Test 3 " + LIST_SEPARATORS[0] * WIDTH)

    if internal_module is None or internal_spec is None:
        return
    internal_module.testKeyBoardInterrupt()


def test_4(internal_spec, internal_module):
    """
    Test number 4.

    Parameters
    ----------
    internal_spec : ModuleSpec
        Object obtained from calling
        "importlib.util.spec_from_file_location()".
    internal_module : Module
        Object obtained from calling "importlib.util.module_from_spec()".

    Returns
    -------
    None.

    """
    print(LIST_SEPARATORS[0] * WIDTH + " Test 4 " + LIST_SEPARATORS[0] * WIDTH)

    if internal_module is None or internal_spec is None:
        return
    internal_module.testSystemExit()


def test_5(internal_spec, internal_module):
    """
    Test number 5.

    Parameters
    ----------
    internal_spec : ModuleSpec
        Object obtained from calling
        "importlib.util.spec_from_file_location()".
    internal_module : Module
        Object obtained from calling "importlib.util.module_from_spec()".

    Returns
    -------
    None.

    """
    print(LIST_SEPARATORS[0] * WIDTH + " Test 5 " + LIST_SEPARATORS[0] * WIDTH)

    if internal_module is None or internal_spec is None:
        return
    internal_module.testOtherException()


def autocorrector(file_path_module: str, file_path_metadata: str = ""):
    """
    Function for the autocorrector to call when evaluaing scripts.

    Parameters
    ----------
    file_path_module : String
        File path of the script to be tested.
    file_path_metadata : String
        File path of the file that will contain the metadata of the batttery
        of tests. The default is "".

    Returns
    -------
    None.

    """
    __spec, __module = module_from_file("Autocorrection", file_path_module)

    __metadata = main(__spec, __module)

    if file_path_metadata != "":
        with open(file_path_metadata, "w", encoding="UTF-8") as file_metadata:
            json.dump(
                __metadata, file_metadata, skipkeys=True, indent=4, sort_keys=True
            )


def main(internal_spec, internal_module) -> dict:
    """
    Executes all the test functions in order anf gathers the metadata of the
    execution.

    Parameters
    ----------
    internal_spec : ModuleSpec
        Object obtained from calling
        "importlib.util.spec_from_file_location()".
    internal_module : Module
        Object obtained from calling "importlib.util.module_from_spec()".

    Returns
    -------
    Dictionary
        Dictionary with different metadata of the battery of tests executed.

    """

    tests = (test_1, test_2, test_5)

    list_commentators = sorted(LIST_COMMENTATORS, key=(len), reverse=True)

    list_separators = sorted(LIST_SEPARATORS, key=(len), reverse=True)

    __metadata = {
        "number_tests": len(tests),
        "list_commentators": list_commentators,
        "list_length_commentators": [len(element) for element in list_commentators],
        "list_separators": list_separators,
        "list_length_separators": [len(element) for element in list_separators],
    }

    for test in tests:
        try:
            test(internal_spec, internal_module)
        except Exception:  # pylint: disable=broad-except
            print(traceback.format_exc())
    return __metadata


if __name__ == "__main__":
    spec, module = module_from_file("Your script", FILE_NAME_OF_YOUR_SCRIPT)

    metadata = main(spec, module)
