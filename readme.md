# Jeff-OS

My terminal os I made for fun

## Usage
Before installing u need to make sure that you have Python 3.0 and Make
Run these commands to make sure you have the libraries
```sh
python --version
make --version
```

First, install the OS by running make install
```sh
make install
```

Then, run the os by running make run
```sh
make run
```

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

## Meta

Distributed under the MIT license. See ``license.txt`` for more information