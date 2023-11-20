# Python tasks autocorrector
This script autoevaluates python tasks. It works executing a battery of tests against the solution and submission for a given task and comparing the outputs.

The battery of tests script, the solution script and the submission script must be in the same directory (folder).

### Setting Directory
To change the directory of the task executed, you must go to the file _"tasks_autocorrector.py"_ and find the section at the start that says:

    ###############################################################################
    #                  WRITE HERE THE FILE PATH TO THE DIRECTORY                  #
    #                      WHERE THE SCRIPTS OF THE TASK ARE                      #
    FILE_PATH_DIRECTORY_SCRIPTS = "test/"
    ###############################################################################

* FILE_PATH_DIRECTORY_SCRIPTS: Is the path to the directory that contains the previous 3 files. Mus end with a _"/"_.

### Setting Files Names
To change the names of the scripts of the task that are inside the directory, you must go to the file _"tasks_autocorrector.py"_ and find the section at the start that says:

    ###############################################################################
    #        WRITE HERE THE FILE NAMES OF THE SCRIPTS OF THE ASSIGNED TASK        #
    FILE_NAME_SCRIPT_BATTERY_OF_TESTS = "test_battery_of_tests.py"
    FILE_NAME_SOLUTION_SCRIPT = "test_solution.py"
    FILE_NAME_SUBMITED_SCRIPT = "test_submission.py"
    ###############################################################################

* FILE_NAME_SCRIPT_BATTERY_OF_TESTS: Is the file name of the script of the battery of tests. File must be a _".py"_ file and contain an "autocorrector()" funtion for the autocrrector be able to call the script.
* FILE_NAME_SOLUTION_SCRIPT: Is the file name of the script that contains the solution. File must be a _".py"_ file.
* FILE_NAME_SUBMITED_SCRIPT: Is the file name of the script that contains the submission. File must be a _".py"_ file.

### Options
This program  contains extra options. To change these must go to the file _"tasks_autocorrector.py"_ and find the section at the start that says:

    ###############################################################################
    #                                 OPTIONS                                     #
    CLEAN_ENVIRONMENT = True
    FILENAME_CONSOLE_OUTPUT_SOLUTION = "output_solution.conlog"
    FILENAME_CONSOLE_OUTPUT_SUBMITED = "output_submited.conlog"
    OVERWRITE = True
    SCORE = False
    WIDTH = 36
    ###############################################################################

* CLEAN_ENVIRONMENT: If True deletes al the files created during the autocorrection. If False keeps them.
* FILENAME_CONSOLE_OUTPUT_SOLUTION: File name of the file where the console output of the execution of the solution script is stored in the FILE_PATH_DIRECTORY_SCRIPTS.
* FILENAME_CONSOLE_OUTPUT_SUBMITED: File name of the file where the console output of the execution of the submitted script is stored in the FILE_PATH_DIRECTORY_SCRIPTS.
* OVERWRITE: If True, in the case that the console output files are found in the FILE_PATH_DIRECTORY_SCRIPTS, it deletes them to overwrite them. If False, in the case that the console output files are found in the FILE_PATH_DIRECTORY_SCRIPTS, it stops the execution of the program.
* SCORE: If True at the end of the execution prints the score, If False at the end of the execution doesn't print the score.
* WIDTH: Width of the visual separators that the programs outputs.
