import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Define the coordinates of the cuboid
cuboid_coordinates = [
    [
        [
            [3.79, 3.83, 0], [3.79, 3.83, 1], [3.79, 3.95, 0], [3.79, 3.95, 1]
        ],
        [
            [3.79, 3.95, 0], [3.79, 3.95, 1], [3.9, 3.95, 0], [3.9, 3.95, 1]
        ],
        [
            [3.9, 3.95, 0], [3.9, 3.95, 1], [3.9, 3.83, 0], [3.9, 3.83, 1]
        ],
        [
            [3.9, 3.83, 0], [3.9, 3.83, 1], [3.79, 3.83, 0], [3.79, 3.83, 1]
        ]
    ],
]

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot each face of the cuboid with different colors
for cuboid in cuboid_coordinates:
    for face in cuboid:
        poly3d = [list(point) for point in face]
        # Assign a random color to each face
        face_color = [float(i) / 255 for i in np.random.randint(0, 256, 3)]
        ax.add_collection3d(Poly3DCollection([poly3d], linewidths=1, edgecolors='black', facecolors=[face_color], alpha=0.5))

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()
