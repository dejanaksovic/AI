import os
import numpy as np

def format_map(map_name: str):
   base_path = os.getcwd()
   file_path = os.path.join(base_path, 'api')
   file_path = os.path.join(file_path, 'maps')
   file_path = os.path.join(file_path, f'{map_name}.txt')
   values = []

   with open(file_path) as f:
      lines = f.readlines()

   for line in lines:
      new_line = line.replace('\n', '')
      chars = new_line.split(',')
      chars.append(0)
      chars.pop(0)
      chars.pop(0)
      values.append(chars)

   for value in values:
      for itter, single_value in enumerate(value):
         value[itter] = int(single_value)
   return values