# padio

Zero pad numeric filenames

Turn a bunch of files like this:

    file1.txt
    file10.txt
    file5.txt

and want them to be sorted like this:

    file01.txt
    file05.txt
    file10.txt

you can run:

    padio *.txt


## Installation

Padio can be run on any system that includes Python 3 after installation with `pip`:

    pip3 install padio

Or by downloading `./padio.py` and placing it anywhere in your `$PATH`.

*Note: I have not tested on Windows, but would welcome feedback or a patch*

## Usage

    usage: padio [-h] [-l LENGTH] [-f] [-v] [-d] [-i REGEX] [--ignore-files IGNOREFILE [IGNOREFILE ...]] file [file ...]

    Pads numbers in file names so they consistently align and sort

    positional arguments:
      file                  Files to be renamed

    optional arguments:
      -h, --help            show this help message and exit
      -l LENGTH, --length LENGTH
                            Length of numbers after padding (default: auto)
      -f, --force           Force rename, even if file at destination exists
      -v, --verbose         Print all actions
      -d, --dry-run         Print actions only without modifying any file. Implies --verbose
      -i REGEX, --ignore REGEX
                            Regular expression used to ignore files matching the name
      --ignore-files IGNOREFILE [IGNOREFILE ...]
                            Files to ignore for renaming. Must add -- before positional arguments

## Original repo

Originally hosted at https://git.iamthefij.com/iamthefij/padio.git
