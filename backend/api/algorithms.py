import numpy as np
import itertools

def greedySearch(matrix):
  working_matrix = np.array(matrix, dtype = "object")
  a, b = working_matrix.shape
  
  coins_allocated = [0] #Pratimo koje smo koine nasli da se ne bismo vracali, a kada niz ima 5 elemenata kraj je igrice i to name je ujedno i put kojim se karakter krece
  curr_index = 0 #Jer uvek je karaket na polju prvog koina, odatle zapocinjemo pretragu

  curr_min = 1000 #za pracenje minimalne vrednosti, inicjalno u teoriji manji broj nego bilo koji da se pojavi
  curr_min_index = 0

  while not len(coins_allocated) == 5:
    for i in range(0, a):
      if working_matrix[curr_index][i] < curr_min and not i in coins_allocated and i != curr_index:
          curr_min_index = i
          curr_min = working_matrix[curr_index][i]
    coins_allocated.append(curr_min_index)
    curr_min = 1000 #RESETAMO MIN

  return coins_allocated
      
def bruteSearch(matrix):
  print("its on")
  matrix_to_work = np.array(matrix)
  init_stack = [1, 2, 3, 4]
  init_visited = [0]

  paths = []
  path_weights = []

  def make_array_possibles(curr_path: list, stack: list) -> list:
    if len(stack) == 1:
      return stack[0]
    
    paths_possible = []

    for stack_item in stack:
      new_stack = list(stack)
      new_stack.remove(stack_item)
      single_new_path = make_array_possibles([curr_path, stack_item], new_stack)
      itertools.chain.from_iterable(single_new_path)

    return paths_possible

  return make_array_possibles([0], init_stack)