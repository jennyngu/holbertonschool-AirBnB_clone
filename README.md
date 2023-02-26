# AirBnB Clone - Command Interpreter


<p align="center">
  <img src="https://i.imgur.com/WqHvIJs.png" alt="Hbton logo">
</p>


This is a command interpreter for managing objects in an AirBnB clone project. It is the first step in building a full web application and is designed to help with HTML/CSS templating, database storage, API, and front-end integration.

## Installation

To install clone the repo with the following command:

```
git clone https://github.com/JennyHolberton/holbertonschool-AirBnB_clone
```

## Usage

How to Use

To use the command interpreter, run the console.py script. This will start a prompt where you can enter commands to manage the objects in the AirBnB project.

The following commands are available:

    create: create a new object
    show: show an object
    destroy: destroy an object
    all: show all objects of a certain type
    update: update an object


The command interpreter can also be run in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Running Unit Tests

To run unit tests for the command interpreter, navigate to the tests directory and run the following command:

```
python3 -m unittest discover
```

## Authors

- [@JennyHolberton](https://github.com/JennyHolberton)

- [@BigBadMatt](https://github.com/bigBadMatt)

- [@wendy-holberton](https://github.com/wendy-holberton)