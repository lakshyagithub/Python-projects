import matplotlib.pyplot as plt

data = [
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 8, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 8, 4, 5],
        [10, 10, 10, 10, 10, 10, 10, 8, 8, 4, 5],
        [10, 10, 10, 10, 10, 10, 8, 8, 8, 4, 5],
        [10, 10, 10, 10, 10, 8, 0, 8, 8, 4, 5],
        [10, 10, 10, 10, 8, 8, 8, 8, 8, 4, 5],
        [10, 10, 10, 8, 8, 0, 8, 8, 8, 4, 5],
        [10, 10, 8, 8, 8, 8, 8, 8, 8, 4, 5],
        [10, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5],
        [10, 10, 5, 5, 5, 5, 5, 5, 5, 5, 10]
        ]

plt.imshow(data, cmap="nipy_spectral")
plt.show()