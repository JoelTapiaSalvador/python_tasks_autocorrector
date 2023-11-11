# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 15:02:29 2023

@author: Joel Tapia Salvador
"""
import os
import sys
import importlib
from argparse import ArgumentParser, HelpFormatter, SUPPRESS
from operator import attrgetter


class CustomHelpFormatter(HelpFormatter):
    """
    A class to format the help information when using the "-h" parameter.


    Methods
    -------
    add_arguments(actions)

    add_usage(self, usage, actions, groups, prefix=None)

    """

    def add_arguments(self, actions):
        """
        Overights of the class HelpFormatter "add_arguments()" method that
        sorts alphabetically the parameters.

        .. warning:: This class is internal and should not be called outside of this class.
        This documention is to guide and inform in the future in case of
        changes needed to be made.

        Parameters
        ----------
        actions : list
            List of argparse actions.

        Returns
        -------
        None.

        """
        actions = sorted(actions, key=attrgetter('option_strings'))
        super().add_arguments(actions)

    def add_usage(self, usage, actions, groups, prefix=None):
        """
        Overights of the class HelpFormatter "add_usage()" method that
        sorts alphabetically the parameters.

        .. warning:: This class is internal and should not be called outside of this class.
        This documention is to guide and inform in the future in case of
        changes needed to be made.

        Parameters
        ----------
        usage : None or str
            "usage" parameter from __init__ call of "ArgumentParser" class.
        actions : list
            List of argparse actions.
        groups : list
            DESCRIPTION.
        prefix : None or str, optional
            DESCRIPTION. The default is None.

        Returns
        -------
        None.

        """
        if prefix is None:
            prefix = 'Usage: '
        super().add_usage(usage, actions, groups, prefix)


class Options(ArgumentParser):
    """
    A class to indicate the parameters options.


    Methods
    -------
    parse():
        Parses the arguments of the program.
    """

    def __init__(self):
        # MODEL SETTINGS
        super().__init__(description="This script autoevaluates python tasks.",
                         add_help=False, formatter_class=CustomHelpFormatter)
        self._positionals.title = 'Positional arguments'
        self._optionals.title = 'Optional arguments'

        # Positional arguments
        super().add_argument('file_path_submited_script', action="store",
                             help='Submited script to be evaluated.')

        super().add_argument('file_path_solution_script', action="store",
                             help='Solution script to be evaluated.')

        super().add_argument('file_path_script_battery_of_tests',
                             action="store",
                             help='File name of the battery of tests for the' +
                             ' task.')
        # Optional arguments
        super().add_argument('-h', '--help', action='help', default=SUPPRESS,
                             help='Show this help message and exit.')

        super().add_argument('-s', '--score',
                             required=False, action="store_true",
                             default=False,
                             help='Show the score of the task.')

        super().add_argument('-ce', '--clean-environment',
                             required=False, action="store_true",
                             default=True,
                             help='Clean the environment after evaluating.')

        super().add_argument('-fcoso', '--file-console-ouput-solution',
                             required=False, action="store",
                             default='output_solution.conlog',
                             help='File name for the console output of the ' +
                             'execution of the solution for the task.')

        super().add_argument('-fcosu', '--file-console-ouput-submited',
                             required=False, action="store",
                             default='output_submited.conlog',
                             help='File name for the console output of the ' +
                             'execution of the sunmission for the task.')

        super().add_argument('-w', '--width', type=int,
                             required=False, action="store",
                             default=36,
                             help='Width visual console separators.')

    def parse(self):
        """
        Parses the arguments of the program.

        Returns
        -------
        Namespace
            Class with all parameters options as properties of the class.

        """
        return super().parse_args()


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


def initialization():
    """
    Initiates the environment for the autocorrection.

    Returns
    -------
    None.

    """
    print("Initializing task autocorrector...\n")

    global SCORE
    global CLEAN_ENVIRONMENT
    global WIDTH
    global SEPARATOR_1
    global SEPARATOR_2
    global SPACER_1
    global SPACER_2
    global FILE_PATH_SUBMITED_SCRIPT
    global FILE_PATH_SOLUTION_SCRIPT
    global FILE_PATH_SCRIPT_BATTERY_OF_TESTS
    global FILENAME_CONSOLE_OUTPUT_SOLUTION
    global FILENAME_CONSOLE_OUTPUT_SUBMITED
    global DEFAULT_OUTPUT

    arguments = Options().parse()

    SCORE = arguments.score
    CLEAN_ENVIRONMENT = arguments.clean_environment
    WIDTH = arguments.width
    SEPARATOR_1 = "=" * (2 * WIDTH + 17)
    SEPARATOR_2 = "*" * WIDTH
    SPACER_1 = "#" * (WIDTH + 5)
    SPACER_2 = "-" * WIDTH
    FILE_PATH_SUBMITED_SCRIPT = arguments.file_path_submited_script
    FILE_PATH_SOLUTION_SCRIPT = arguments.file_path_solution_script
    FILE_PATH_SCRIPT_BATTERY_OF_TESTS = arguments.file_path_script_battery_of_tests
    FILENAME_CONSOLE_OUTPUT_SOLUTION = arguments.file_console_ouput_solution
    FILENAME_CONSOLE_OUTPUT_SUBMITED = arguments.file_console_ouput_submited

    DEFAULT_OUTPUT = sys.stdout


def evaluate_solution(module_battery_of_tests):
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
    with open(FILENAME_CONSOLE_OUTPUT_SOLUTION, 'w', encoding="UTF-8") as file:
        sys.stdout = file
        module_battery_of_tests.autocorrector(FILE_PATH_SOLUTION_SCRIPT)
    sys.stdout = DEFAULT_OUTPUT


def evaluate_submission(module_battery_of_tests):
    """
    Evaluates the battery of tests onto the submitted script.

    Parameters
    ----------
    battery_of_tests : module
        Module with the battery of tests. Must have a main() function that
        initiates the battery of tests onto the submitted script.

    Returns
    -------
    None.

    """
    print("Evaluating submission...\n")
    with open(FILENAME_CONSOLE_OUTPUT_SUBMITED, 'w', encoding="UTF-8") as file:
        sys.stdout = file
        module_battery_of_tests.autocorrector(FILE_PATH_SUBMITED_SCRIPT)
    sys.stdout = DEFAULT_OUTPUT


def compare_results(module_battery_of_tests):
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
    with open(FILENAME_CONSOLE_OUTPUT_SOLUTION, "r", encoding="UTF-8") as file_console_output_solution, open(FILENAME_CONSOLE_OUTPUT_SUBMITED, "r", encoding="UTF-8") as file_console_output_submission:
        for line_file_console_output_solution, line_file_console_output_submission in zip(file_console_output_solution, file_console_output_submission):
            if line_file_console_output_solution[0] == module_battery_of_tests.SEPARATOR:
                print(line_file_console_output_solution)
            else:
                count += 1
                line_file_console_output_solution = line_file_console_output_solution.replace(
                    "\n", "")
                line_file_console_output_submission = line_file_console_output_submission.replace(
                    "\n", "")
                print(SEPARATOR_1)
                if line_file_console_output_solution == line_file_console_output_submission:
                    print(SPACER_1 + " RIGHT " + SPACER_1)
                    grade += 1
                else:
                    print(SPACER_1 + " WRONG " + SPACER_1)
                    print(SPACER_2 + " EXPECTED OUTPUT " + SPACER_2)
                    print(line_file_console_output_solution)
                    print(SPACER_2 + " OBTAINED RESULT " + SPACER_2)
                    print(line_file_console_output_submission)
        print(SEPARATOR_1 + "\n")

    if SCORE and count != 0:
        print(SEPARATOR_2)
        print("SCORE :=> " + str(grade) + " / " + str(count) +
              " ==> " + str(grade / count * 100) + "%")
        print(SEPARATOR_2 + "\n")


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
        os.remove(FILENAME_CONSOLE_OUTPUT_SOLUTION)
        os.remove(FILENAME_CONSOLE_OUTPUT_SUBMITED)


if __name__ == "__main__":
    initialization()

    battery_of_tests = module_from_file(
        "battery_of_test", FILE_PATH_SCRIPT_BATTERY_OF_TESTS)

    evaluate_solution(battery_of_tests)

    evaluate_submission(battery_of_tests)

    compare_results(battery_of_tests)

    clean_environment()

    print("Finished.")
