# Usage:
#   python tester.py -p <path to a directory> -f <function name> 
# 

import cv2
import argparse

import operation_loader

# Construct the argument parser and parse the arguments
def parseArgs():
  ap = argparse.ArgumentParser(description="Loader test")
  ap.add_argument("-p", "--path", required = False,
  default = "./test",
	help = "path to a directory from where a module with the function is located")
  ap.add_argument("-f", "--func", required = False,
  default = "testmodule.printkwargs",
	help = "a function name (module.func) that will be loaded")

  args = ap.parse_args()   
  kwargs = dict((k,v) for k,v in vars(args).items() if k!="message_type")
  
  return kwargs


# Main function
def main(**kwargs):
  # Set sytem path where from a function(s) will by loaded
  operation_loader.set_sytem_path(kwargs['path'])
  f = operation_loader.get(kwargs['func'])
  tkwargs = {}
  tkwargs['ke1'] = 'value1'
  tkwargs['ke2'] = 'value2'
  tkwargs['ke3'] = 'value3'
  f(None, **tkwargs)


# Entry point
if __name__ == "__main__":
    kwargs = parseArgs()
    main(**kwargs) 
