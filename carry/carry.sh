#!/bin/bash

PKG="carry"
DIR="/tmp/.carry"

function help {
    echo "\
Usage: carry -c [FILE]...
   or: carry -c [DIRECTORY]...
   or: carry -d

Mandatory arguments to long options are mandatory for short options too.
  -c, --carry          add files/directories path to the buffer
  -d, --drop           move files/directories to the current directory

  -h, --help           display this help and exit"
}

function carry {
    # Loop through arguments
    for arg in "$@"; do
	# Save full path only if file exists
	if [[ -e "$arg" ]]; then
	    echo "$(realpath $arg)" >> $DIR
	else
	    echo "$PKG: $arg: No such file or directory"
	fi
    done
}

function drop {
    exit
}

function main {

    while [ ! $# -eq 0 ]; do
	case $1 in
	    -c | --carry)
		shift; carry "$@"; break;;

	    -d | --drop)
		shift; drop "$@"; break;;

	    -h | --help)
		help; break;;

	    *)
		help; exit 1;;
	esac
    done

    exit 0
}

main "$@"
exit 0
