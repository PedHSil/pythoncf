from sys import path

from modulopy import modulo
#import modulopy.modulo import  importa apenas o modulo(função) que escolhemos 

test = [
  ['A', 'B', 'C', 'D'],
  ['E', 'F', 'G', 'H'],
  ['I', 'J', 'K', 'L'],
  ['M', 'N', 'O', 'P']
]

# print an ASCII grid around the given 2D array
# axis booleans decide whether or not to print row/column labels

def print_grid(grid, xAxis=False, yAxis=False):
  if xAxis:
    column_labels = ' | '.join(str(i + 1) for i in range(len(grid[0])))
    print(f"{'   | ' if yAxis else '| '}{column_labels} |")
  for row_num, row in enumerate(grid):
    row_str = ' | '.join(str(i) for i in row)
    print(f"{'---' if yAxis else ''}{'+---' * len(grid[0])}+")
    print(f"{' ' + str(row_num + 1) + ' ' if yAxis else ''}| {row_str} |")
  print(f"{'---' if yAxis else ''}{'+---' * len(grid[0])}+")

print_grid(test, False, False)
print()
print_grid(test, True, False)
print()
print_grid(test, False, True)
print()
print_grid(test, True, True)