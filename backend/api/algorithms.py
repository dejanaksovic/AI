import numpy as np

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
  
  print(f"HERE: {coins_allocated}")

  return coins_allocated
      
  

    