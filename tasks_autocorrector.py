# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 15:02:29 2023

@author: Joel Tapia Salvador
"""
import os
import sys
import importlib

###############################################################################
#                  WRITE HERE THE FILE PATH TO THE DIRECTORY                  #
#                      WHERE THE SCRIPTS OF THE TASK ARE                      #
FILE_PATH_DIRECTORY_SCRIPTS = "test/"
###############################################################################

###############################################################################
#        WRITE HERE THE FILE NAMES OF THE SCRIPTS OF THE ASSIGNED TASK        #
FILE_NAME_SCRIPT_BATTERY_OF_TESTS = "test_battery_of_tests.py"
FILE_NAME_SOLUTION_SCRIPT = "test_solution.py"
FILE_NAME_SUBMITED_SCRIPT = "test_submission.py"
###############################################################################

###############################################################################
#                                   OPTIONS                                   #
CLEAN_ENVIRONMENT = True
FILENAME_CONSOLE_OUTPUT_SOLUTION = "output_solution.conlog"
FILENAME_CONSOLE_OUTPUT_SUBMITED = "output_submited.conlog"
OVERWRITE = True
PREV_IS_SEPARATOR = True
SCORE = True
WIDTH = 36
###############################################################################


def check_environment():
    """
    Checks if the environment is in proper state for executing the
    autocorrector.

    Raises
    ------
    NotADirectoryError
        The FILE_PATH_DIRECTORY_SCRIPTS give is not a director or
        doesn't exists.
    FileNotFoundError
        Either FILE_NAME_SCRIPT_BATTERY_OF_TESTS or FILE_NAME_SOLUTION_SCRIPT
        or FILE_NAME_SUBMITED_SCRIPT are not a file or doesn't exist in the
        FILE_PATH_DIRECTORY_SCRIPTS.
    FileExistsError
        OVERWRITE is False and either FILENAME_CONSOLE_OUTPUT_SOLUTION or
        FILENAME_CONSOLE_OUTPUT_SUBMITED exist as files in
        FILE_PATH_DIRECTORY_SCRIPTS.

    Returns
    -------
    None.

    """
    print("Checking environment...\n")
    if not os.path.isdir(FILE_PATH_DIRECTORY_SCRIPTS):
        raise NotADirectoryError("File path is not a directoryñ.")
    if not os.path.isfile(FILE_PATH_DIRECTORY_SCRIPTS
                          + FILE_NAME_SCRIPT_BATTERY_OF_TESTS):
        raise FileNotFoundError("Script battery of tests not found: " +
                                FILE_PATH_DIRECTORY_SCRIPTS
                                + FILE_NAME_SCRIPT_BATTERY_OF_TESTS)
    if not os.path.isfile(FILE_PATH_DIRECTORY_SCRIPTS
                          + FILE_NAME_SOLUTION_SCRIPT):
        raise FileNotFoundError("Script solution not found: " +
                                FILE_PATH_DIRECTORY_SCRIPTS
                                + FILE_NAME_SOLUTION_SCRIPT)
    if not os.path.isfile(FILE_PATH_DIRECTORY_SCRIPTS
                          + FILE_NAME_SUBMITED_SCRIPT):
        raise FileNotFoundError("Script submission not found: " +
                                FILE_PATH_DIRECTORY_SCRIPTS
                                + FILE_NAME_SUBMITED_SCRIPT)
    if os.path.isfile(FILE_PATH_DIRECTORY_SCRIPTS
                      + FILENAME_CONSOLE_OUTPUT_SOLUTION):
        if OVERWRITE:
            os.remove(FILE_PATH_DIRECTORY_SCRIPTS +
                      FILENAME_CONSOLE_OUTPUT_SOLUTION)
        else:
            raise FileExistsError(
                "Console output file for solution already exists."
                + FILE_PATH_DIRECTORY_SCRIPTS
                + FILENAME_CONSOLE_OUTPUT_SOLUTION)
    if os.path.isfile(FILE_PATH_DIRECTORY_SCRIPTS
                      + FILENAME_CONSOLE_OUTPUT_SUBMITED):
        if OVERWRITE:
            os.remove(FILE_PATH_DIRECTORY_SCRIPTS +
                      FILENAME_CONSOLE_OUTPUT_SUBMITED)
        else:
            raise FileExistsError(
                "Console output file for submission already exists."
                + FILE_PATH_DIRECTORY_SCRIPTS
                + FILENAME_CONSOLE_OUTPUT_SUBMITED)


def clean_environment():
    """
    If the global variable CLEAN_ENVIRONMENT is true this functions cleans all
    files created during the evaluation from the current environment.

    Returns
    -------
    None.

    """
    if CLEAN_ENVIRONMENT:
        print("Cleaning environment...\n")
        os.remove(FILE_PATH_DIRECTORY_SCRIPTS +
                  FILENAME_CONSOLE_OUTPUT_SOLUTION)
        os.remove(FILE_PATH_DIRECTORY_SCRIPTS +
                  FILENAME_CONSOLE_OUTPUT_SUBMITED)
        if os.path.isdir(FILE_PATH_DIRECTORY_SCRIPTS + "__pycache__"):
            for file_name in os.listdir(FILE_PATH_DIRECTORY_SCRIPTS
                                        + "__pycache__"):
                os.remove(FILE_PATH_DIRECTORY_SCRIPTS +
                          "__pycache__/" + file_name)
            os.rmdir(FILE_PATH_DIRECTORY_SCRIPTS + "__pycache__")
        if os.path.isdir("__pycache__"):
            for file_name in os.listdir("__pycache__"):
                os.remove("__pycache__/" + file_name)
            os.rmdir("__pycache__")


def compare_results():
    """
    Compares the output of the submitted script against the output of the
    solution script.

    Returns
    -------
    None.

    """
    print("Comparing results...\n")
    count = 0
    grade = 0
    with open(FILE_PATH_DIRECTORY_SCRIPTS + FILENAME_CONSOLE_OUTPUT_SOLUTION, "r", encoding="UTF-8") as file_console_output_solution, open(FILE_PATH_DIRECTORY_SCRIPTS + FILENAME_CONSOLE_OUTPUT_SUBMITED, "r", encoding="UTF-8") as file_console_output_submission:
        for line_file_console_output_solution, line_file_console_output_submission in zip(file_console_output_solution, file_console_output_submission):
            line_file_console_output_solution \
                = line_file_console_output_solution.replace("\n", "")
            line_file_console_output_submission \
                = line_file_console_output_submission.replace("\n", "")
            if line_file_console_output_solution[0] in MODULE_BATTERY_OF_TESTS.LIST_SEPARATORS or line_file_console_output_solution[:3] in MODULE_BATTERY_OF_TESTS.LIST_COMMENTATORS:
                print_with_separators(line_file_console_output_solution)
            else:
                count += 1

                if line_file_console_output_solution \
                        == line_file_console_output_submission:
                    print_with_separators(
                        LIST_SPACERS[0] + " RIGHT " + LIST_SPACERS[0])
                    grade += 1
                else:
                    print_with_separators(
                        LIST_SPACERS[0] + " WRONG " + LIST_SPACERS[0] + "\n"
                        + LIST_SPACERS[1] +
                        " EXPECTED OUTPUT " + LIST_SPACERS[1] + "\n"
                        + line_file_console_output_solution + "\n"
                        + LIST_SPACERS[1] + " OBTAINED RESULT " +
                        LIST_SPACERS[1] + "\n"
                        + line_file_console_output_submission)
        print()

    if SCORE and count != 0:
        print(LIST_SEPARATORS[1])
        print("SCORE ==> " + str(grade) + " / " + str(count) +
              "\nPERCENTAGE ==> " + str(grade / count * 100) + "%")
        print(LIST_SEPARATORS[1] + "\n")


def evaluate_solution():
    """
    Evaluates the battery of tests onto the solution script.

    Parameters
    ----------
    battery_of_tests : Python module
        Module with the battery of tests. Must have a "autocorrector()"
        function that initiates the battery of tests onto the submitted script.

    Returns
    -------
    None.

    """
    print("Evaluating solution...\n")
    with open(FILE_PATH_DIRECTORY_SCRIPTS
              + FILENAME_CONSOLE_OUTPUT_SOLUTION, 'w',
              encoding="UTF-8") as file:
        sys.stdout = file
        MODULE_BATTERY_OF_TESTS.autocorrector(
            FILE_PATH_DIRECTORY_SCRIPTS + FILE_NAME_SOLUTION_SCRIPT)
    sys.stdout = DEFAULT_OUTPUT


def evaluate_submission():
    """
    Evaluates the battery of tests onto the submitted script.

    Parameters
    ----------
    battery_of_tests : module
        Module with the battery of tests. Must have a "autocorrector()"
        function that initiates the battery of tests onto the submitted script.

    Returns
    -------
    None.

    """
    print("Evaluating submission...\n")
    with open(FILE_PATH_DIRECTORY_SCRIPTS
              + FILENAME_CONSOLE_OUTPUT_SUBMITED, 'w',
              encoding="UTF-8") as file:
        sys.stdout = file
        MODULE_BATTERY_OF_TESTS.autocorrector(
            FILE_PATH_DIRECTORY_SCRIPTS + FILE_NAME_SUBMITED_SCRIPT)
    sys.stdout = DEFAULT_OUTPUT


def initialization():
    """
    Initiates the environment for the autocorrection.

    Returns
    -------
    None.

    """
    global DEFAULT_OUTPUT
    global LIST_SEPARATORS
    global LIST_SPACERS
    global MODULE_BATTERY_OF_TESTS

    print("Initializing task autocorrector...\n")

    DEFAULT_OUTPUT = sys.stdout

    LIST_SEPARATORS = ["-" * (2 * WIDTH + 17), "*" * WIDTH]
    LIST_SPACERS = ["#" * (WIDTH + 5), "-" * WIDTH]

    MODULE_BATTERY_OF_TESTS = module_from_file(
        "battery_of_test", FILE_PATH_DIRECTORY_SCRIPTS +
        FILE_NAME_SCRIPT_BATTERY_OF_TESTS)


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
    module : python module
        Python module object.

    """
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def print_with_separators(text):
    """


    Parameters
    ----------
    text : str
        DESCRIPTION.

    Returns
    -------
    None.

    """
    global PREV_IS_SEPARATOR
    if not PREV_IS_SEPARATOR:
        print(LIST_SEPARATORS[0])
        PREV_IS_SEPARATOR = True
    else:
        PREV_IS_SEPARATOR = False
    print(text)
    if not PREV_IS_SEPARATOR:
        print(LIST_SEPARATORS[0])
        PREV_IS_SEPARATOR = True
    else:
        PREV_IS_SEPARATOR = False


if __name__ == "__main__":
    check_environment()

    initialization()

    evaluate_solution()

    evaluate_submission()

    compare_results()

    clean_environment()

    print("Finished.")
