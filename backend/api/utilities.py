import os
import numpy as np

def format_map(map_name: str):
   base_path = os.getcwd()
   file_path = os.path.join(base_path, 'api')
   file_path = os.path.join(file_path, 'maps')
   file_path = os.path.join(file_path, f'{map_name}.txt')

   with open(file_path) as f:
      lines = f.readlines()

   values = np.zeros((len(lines), len(lines)))

   for linIndex, line in enumerate(lines):
      line = line.replace('\n', '')
      values[linIndex][linIndex] = 0
      for valueIndex, value in enumerate(line.split(',')):
         if valueIndex > 1 and valueIndex < 5:
            values[linIndex-2][valueIndex] = int(value)
            values[valueIndex][linIndex - 2] = int(value)

   return values