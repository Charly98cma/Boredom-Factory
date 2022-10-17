#!/bin/bash

PKG="carry"
DIR="/tmp/.carry"

function help {
    echo "\
Usage: $PKG -c [FILE]... [DIRECTORY]...
   or: $PKG -d
   or: $PKG -r

Mandatory arguments to long options are mandatory for short options too.
  -c, --carry          add files/directories path to the path buffer
  -d, --drop           move files/directories to the current directory
  -h, --help           display this help and exit
  -r, --reset	       delete all entries on path buffer"
}

# Add files that exists to the buffer file
function carry {
    # Loop through arguments
    for arg in $@; do
	# Save full path only if file exists
	if [[ -e $arg ]]; then
	    echo $(realpath $arg) >> $DIR
	else
	    echo "\
$PKG: cannot carry $arg: No such file or directory
$PKG: No files or directories stored"
	    reset
	    break
	fi
    done
}

# Delete buffer file contents
function reset {
    truncate -s 0 $DIR
}

# Move files on the buffer to the current directory
function drop {
    cat $DIR | while read line; do
		mv $line $PWD
    done
}

function main {
    # Parse flags and parameters
    while [ ! $# -eq 0 ]; do
		case $1 in
			-c | --carry)
			shift; carry $@; break;;

			-d | --drop)
			shift; drop $@; reset; break;;

			-r | --reset)
			reset; break;;

			-h | --help)
			help; break;;

			*)  # Non-supported flags show help
			help; exit 1;;
		esac
    done
    # Good exit
    exit 0
}

main $@
