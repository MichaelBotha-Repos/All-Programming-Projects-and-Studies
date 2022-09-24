To run the program:
    1.) Ensure that data entered into the relevant Stop Sequence text
        file is in the correct format. The program tries to accommodate 
        us much as possible for stray spaces and newline characters 
        however there still needs to be validation which is as strict as possible.
        Therefore, input data as: 
        [station_name1, True]
        [station_name2, False] 
        [station_name_n, Bool]
        where there are no leading spaces, and no spaces after the Bool 
        but only a newline/"enter" character.

    2.) Open a PowerShell session and navigate to the directory housing the 
        program.

    3.) Select/run the "display_train_stop_sequence.exe" leave a space and enter the 
        file path of the Stop Sequence tex file. If it is in the same directory
        as the program simply enter .\textfile.txt 