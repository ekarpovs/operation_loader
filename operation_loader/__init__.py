import sys
import types
from importlib import import_module


def set_sytem_path(path):
  sys.path.append(path)
  return


def get(full_name):
  func_name = ''
  try:
    if '.' in full_name:
        module_name, func_name = full_name.rsplit('.', 1)
    else:
        module_name = func_name = full_name

    module = import_module(module_name, package=__name__)
    func = getattr(module, func_name)

  except (AttributeError, ModuleNotFoundError):
    raise ImportError('{} is not part of our modules collection!'
          .format(module_name))
  return func


def get_module_meta(module_name):
  mod = import_module(module_name, package=__name__)
  func_names = []
  func_metas = []
  for key, value in mod.__dict__.items():
    if isinstance(value, types.FunctionType):
      fnname = value.__name__
      if fnname[0] != '_':    # private functions
        func_names.append(fnname)
        func_metas.append({'name': fnname, 'doc': value.__doc__})
  return {'descr': mod.__doc__, 'func': func_names, 'meta': func_metas}


def parse_oper_doc(doc):
  lines = doc.strip().split('\n')
  lines = [line.expandtabs().strip() for line in lines if len(line) > 0]
  idx_s = lines.index('Parameters:')
  description = lines[0:idx_s]
  idx_e = lines.index('Returns:')
  parameters = lines[idx_s + 1: idx_e]
  returns_doc = lines[idx_e + 2:]
  idx_s = parameters.index('- params:')
  idx_e = parameters.index('- data:')
  params_doc = parameters[idx_s + 1: idx_e]
  data_doc = parameters[idx_e + 1:]
  return (description, params_doc, data_doc, returns_doc)
