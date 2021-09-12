import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Turning Mario into Luigi

def main():
  mario = mpimg.imread("./mario_big.png")

  (rows, cols, _) = mario.shape
  luigi = np.copy(mario)

  red, green, blue, alpha = 0, 1, 2, 3
  red_tolerance = .9
  green_tolerance = .1
  blue_tolerance = .1

  for row in range(rows):
    for col in range(cols):
      luigi[row, col] = mario[row, col]
      if luigi[row, col, alpha] == 1 and luigi[row, col, red] > red_tolerance and luigi[row, col, green] < green_tolerance and luigi[row, col, blue] < blue_tolerance:
        luigi[row, col, red] = 0
        luigi[row, col, green] = 1
        luigi[row, col, blue] = 0

  fig = plt.figure(figsize=(10, 10))

  fig.add_subplot(1, 2, 1)
  plt.imshow(mario)

  fig.add_subplot(1, 2, 2)
  plt.imshow(luigi)

  plt.show()

if __name__ == "__main__":
  main()
