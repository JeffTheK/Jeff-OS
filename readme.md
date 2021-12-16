# Jeff-OS

Jeff-OS is a pseudo operating system made in python 3

## Requirements
Make,
Python 3.6
GCC

## Usage
Before installing u need to make sure that you have Python 3.6 and Make

Run these commands to make sure you have the libraries
```sh
python --version
make --version
gcc --version
```

First, install the OS by running make install
```sh
make install
```

Then, run the os by running make run
```sh
make run
```

note: `make install` will reinstall the system if it's already present

## How it works
`install.py` installs the os into current folder in `Jeff-OS`, including `boot.py`

`boot.py` launches `/sys/bin/cmd` - our command line, the core of our system.
From there you can launch any binary located in `/sys/bin/`

## File structure
```
Jeff-OS
    ----sys             system files
        ----bin         built in binaries/apps
        ----lib         libraries
        ----var         configs
    ----usr             user files
        ----var         configs

```

## Built-in Apps/Binaries
Source code is located in `src/bin/`

todo: these apps are very basic and have almost no arguments/checks
You can help the project by polishing them.
* apps        -  lists installed binaries
* cat         -  outputs contents of a file
* cd          -  changes directory
* clear       -  clears cmd
* cp          -  copies file
* cmd         -  command line
* find        -  searches in files
* help        -  prints general help
* jobs        -  prints background processes
* ls          -  lists files in dir
* mkdir       -  creates dir
* mv          -  moves files/dirs
* my          -  launches command outside of Jeff-OS
* pwd         -  prints working dir
* rm          -  removes files/dirs
* sleep       -  sleeps for seconds
* touch       -  creates empty text file
* tree        -  recursively lists directories
* uninstall   -  uninstalls binaries
* watch       -  runs command with time period

## Built-in Libraries
Source code is located in `src/lib`
jeffos python package is used to access system info
(right now it's only useful for changing directory since os.chdir() won't work)

## Meta

Distributed under the MIT license. See ``license.txt`` for more information
