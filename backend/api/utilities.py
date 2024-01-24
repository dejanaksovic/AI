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
      for valueIndex, value in enumerate(line.split(',')):
         if valueIndex > 1 and valueIndex < 5:
            values[linIndex][valueIndex-2] = int(value)
            print(f"Setting: [{linIndex}][{valueIndex-2}]")
            values[valueIndex-2][linIndex] = int(value)
            print(f"Setting: [{valueIndex-2}][{linIndex}]\n\n")
      values[linIndex][linIndex] = 0

   return values