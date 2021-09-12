import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.colors import LinearSegmentedColormap

cdict = {
    'red':   [
      [0.0,   0.0,  0.0],
      [0.2,   0.0,  .14],
      [0.75,  1.0,  1.0],
      [1.0,   0.7,  0.7]
    ],
    'green': [
      [0.0,   0.0,  0.14],
      [0.24,  0.14, 0.24],
      [0.3,   0.7,  0.7],
      [0.4,   0.3,  0.0],
      [1.0,   0.0,  0.0]
    ],
    'blue':[
      [0.0,   1.0,  1.0],
      [0.28,  0.0,  0.0],
      [1.0,   0.0,  0.0]
    ]
  }

def mars_colormap(data):
  newcmp = LinearSegmentedColormap('testCmap', segmentdata=cdict, N=256)
  rgba = newcmp(data)

  return rgba

def main():
  mars_gray = mpimg.imread('mars.png')

  lum_img = mars_gray[:, :, 0]

  mars_red = mars_colormap(lum_img)

  plt.imshow(mars_red)
  plt.show()


if __name__ == "__main__":
  main()
