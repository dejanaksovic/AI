import os
import numpy as np

def format_map_values(map_name: str):
   base_path = os.getcwd()
   file_path = os.path.join(base_path, 'api')
   file_path = os.path.join(file_path, 'maps')
   file_path = os.path.join(file_path, f'{map_name}.txt')

   with open(file_path) as f:
      lines = f.readlines()

   matrix_weight = np.zeros((len(lines), len(lines)))
   coin_positions = np.zeros((len(lines), 2))

   for linIndex, line in enumerate(lines):
      line = line.replace('\n', '')
      for valueIndex, value in enumerate(line.split(',')):
         # getting positions
         if valueIndex < 2:
            coin_positions[linIndex][valueIndex] = value

         if valueIndex > 1 and valueIndex < 5:
            matrix_weight[linIndex][valueIndex-2] = int(value)
            matrix_weight[valueIndex-2][linIndex] = int(value)

      matrix_weight[linIndex][linIndex] = 0

   return (coin_positions, matrix_weight)

