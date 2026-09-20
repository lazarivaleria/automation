# Automation

This repository contains Shell scripts created for Laboratory Work 1.

The purpose of the project is to learn how to create and execute simple Shell scripts for automating routine tasks in Linux.


# Cleanup Script
## Description

The `cleanup.sh` script is used to delete temporary files from a specified directory.

By default, the script deletes files with the `.tmp` extension.

The user can also specify other file extensions that should be deleted.

## Usage

```bash
./cleanup.sh <directory> [extension ...]

Examples:

Delete .tmp files:

./cleanup.sh /path/to/directory

Delete .log files:

./cleanup.sh /path/to/directory log

Delete .tmp and .log files:

./cleanup.sh /path/to/directory tmp log

The script checks whether the specified directory exists and displays an error message if it does not.

At the end, the script displays the number of deleted files.


