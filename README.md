# Image Processing Workshop Operation Loader

## It is a part of the [Image Processing Workshop](https://github.com/ekarpovs/image-processing-workshop) project. The package loads an operation (function) from a module that implement an image-processing algorthms without additional coding

### File system structure

    Anywhere in a file system:
_____
    |
    |__ /modules/ __ Python scripts that implemented sets of simple image-processing operations
    |    |
    |    |__init__.py - the 'modules' package declaration
    |   

This package:
_____
    |__ /operation_loader/ The package files
    |


## Local Installation

    - Change dir to operation_loader
    - Run the command:
    ```bash
    pip install -e .
    ```
  

## Usage

    - In a script:
      - import operation_loader;
      - set system path to all modules that will be used: operation_loader.set_sytem_path(path);
      - load a function from a module: f = operation_loader.get(module.func)
      - use the loaded fuction in the script without additional coding.

## Run test

    ```bash
    python tester.py -p <path to a directory where a module is located> -f <function name in form module.func>
    ```
