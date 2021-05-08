'''
Simple operations for test loader factory
'''


def printkwargs(step, **kwargs):
  '''
  Prints kwargs.

  Keyword arguments:
  - Any

  Step arguments:
   - None

  Returns:
  - the kwargs as is.
  '''

  [print(k, v) for k, v in kwargs.items() if k != "image" and k != "orig"]
  
  return kwargs

