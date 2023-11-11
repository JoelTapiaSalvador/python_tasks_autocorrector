# Python tasks autocorrector
 Autocorrector for due tasks in python.

### Usage 
    tasks_autocorrector.py [-h] file_path_submited_script file_path_solution_script file_path_script_battery_of_tests [-s] [-ce] [-fcoso FILE_CONSOLE_OUPUT_SOLUTION] [-fcosu FILE_CONSOLE_OUPUT_SUBMITED] [-w WIDTH]

This script autoevaluates python tasks.

### Positional arguments
    file_path_submited_script
                        Submited script to be evaluated.
    file_path_solution_script
                        Solution script to be evaluated.
    file_path_script_battery_of_tests
                        File name of the battery ofvtests for the task.

### Options
    -ce, --clean-environment
                        Clean the environment after evaluating.
    -fcoso FILE_CONSOLE_OUPUT_SOLUTION, --file-console-ouput-solution FILE_CONSOLE_OUPUT_SOLUTION
                        File name for the console output of the execution of the solution for the task.
    -fcosu FILE_CONSOLE_OUPUT_SUBMITED, --file-console-ouput-submited FILE_CONSOLE_OUPUT_SUBMITED
                        File name for the console output of the execution of the submission for the task.
    -h, --help          Show this help message and exit.
    -s, --score         Show the score of the task.
    -w WIDTH, --width WIDTH
                        Width visual console separators.
