ASSIGNMENT 2
NAME: Yashodhan Vijay Kumthekar
UTA ID: 1001544391

CODE STRUCTURE:
    MinMaxTree class handles creation and evaluation of the search tree.

    getDecision() function is to be called with the gameboard argument to get the next best move for current state.

    getMin and getMax functions calculate the subsequent min and max values for each printGameBoardToFile

    getUtilityValue() function calculates the utility value for the terminal nodes, description in eval_explanation.txt

    the maxConnect4.py is the driver and is used to toggle the interactive and one move mode.




COMPILATION AND EXECUTION:
    To compile for single move mode:
        python maxconnect4.py one-move input1.txt output1.txt

        Output is printed in output argument file

    To compile for interactive mode:
        python maxconnect4.py interactive [input_file] [computer-next/human-next] [depth]

        Output for computer player is in computer.txt
        Output for Human player is in human.txt

DEPTH TIME MAPPING:
    It is in depth-time map.pdf

    Have used the following Terminal command to generate the raw output in time.xlsx
    $> for i in {1..15}; do { echo ${i} && time python maxconnect4.py one-move input1.txt output1.txt ${i}; } 2>&1 |  cat >> time.xlsx;  done;

The code runs on omega
