# function takes in two multidimensional arrays and returns the tensor product of the two arrays
def tensor_product(x, y):
  x_row = len(x)
  x_col = len(x[0])
  y_row = len(y)
  y_col = len(y[0])

  num_rows = x_row * y_row
  num_col = x_col * y_col

  z = [[0] * num_col for i in range(num_rows)] # creates a blank array of the right size

  for i in range(num_rows):
    for j in range(num_col):
      z[i][j] = x[int(i/y_row)][int(j/y_col)] * y[i%y_row][j%y_col]

  return z