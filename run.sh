#!/bin/cmd
# Path: run.sh

PS3= 'Please enter your choice: '
options=("1. Tree viewer" "2. Add Investors" "3.#" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "1. Tree viewer")
            exec python tree_viewer.py
            ;;
        "2. Add Investors")
        read -r -p "Press any key to continue!: " response
        response=${response,,}    # tolower
            exec python execute.py
            ;;
        "3.#")
            echo "you chose choice $REPLY which is $opt"
            ;;
        "Quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done
